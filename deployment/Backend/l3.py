# limit the number of cpus used by high performance libraries
import datetime
import json
import os
import sqlite3

import threading
from threading import Thread

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
sys.path.insert(0, './yolov5')

import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn

from yolov5.models.experimental import attempt_load
from yolov5.utils.downloads import attempt_download
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.datasets import LoadImages, LoadStreams
from yolov5.utils.general import (LOGGER, check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 deepsort root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
count = 0
data = []


def detect():
        with torch.no_grad():
            startTime = datetime.datetime.utcnow()
            yolo_model = 'models/yolov5n.pt'
            deep_sort_model = 'osnet_x0_25'
            source = 3
            output = 'inference/output'
            imgsz = 480
            img = 480
            img_size = 480
            conf_thres = 0.5
            iou_thres = 0.5
            fourcc = 'mp4v'
            device = ''
            show_vid = True
            save_vid = True
            save_txt = True
            classes = [1,2]
            agnostic_nms = True
            augment = True
            evaluate = False
            config_deepsort = "deep_sort/configs/deep_sort.yaml"
            half = True
            visualize = False
            max_det = 1000
            dnn = True
            project = ROOT / 'runs/track'
            name = 'exp'
            exist_ok = False
            webcam = 3 

            # initialize deepsort
            cfg = get_config()
            cfg.merge_from_file(config_deepsort)
            deepsort = DeepSort(deep_sort_model,
                                max_dist=cfg.DEEPSORT.MAX_DIST,
                                max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                                max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                                use_cuda=True)

            # Initialize
            device = select_device(device)
            half &= device.type != 'cpu'  # half precision only supported on CUDA

            # Directories
            save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
            save_dir.mkdir(parents=True, exist_ok=True)  # make dir

            # Load model
            device = select_device(device)
            model = DetectMultiBackend(yolo_model, device=device, dnn=dnn)
            stride, names, pt, jit, _ = model.stride, model.names, model.pt, model.jit, model.onnx
            imgsz = check_img_size(imgsz, s=stride)  # check image size

            # Half
            half &= pt and device.type != 'cpu'  # half precision only supported by PyTorch on CUDA
            if pt:
                model.model.half() if half else model.model.float()

            # Set Dataloader
            vid_path, vid_writer = None, None
            # Check if environment supports image displays
            if show_vid:
                show_vid = check_imshow()

            # Dataloader
            if webcam:
                show_vid = check_imshow()
                cudnn.benchmark = True  # set True to speed up constant image size inference
                dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt and not jit)
                bs = len(dataset)  # batch_size
            else:
                dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt and not jit)
                bs = 1  # batch_size
            vid_path, vid_writer = [None] * bs, [None] * bs

            # Get names and colors
            names = model.module.names if hasattr(model, 'module') else model.names

            # extract what is in between the last '/' and last '.'
            txt_file_name = source.split('/')[-1].split('.')[0]
            txt_path = str(Path(save_dir)) + '/' + txt_file_name + '.txt'

            if pt and device.type != 'cpu':
                model(torch.zeros(1, 3, *imgsz).to(device).type_as(next(model.model.parameters())))  # warmup
            dt, seen = [0.0, 0.0, 0.0, 0.0], 0
            
            for frame_idx, (path, img, im0s, vid_cap, s) in enumerate(dataset): # So this for loop is acting as while
                t1 = time_sync()
                img = torch.from_numpy(img).to(device)
                img = img.half() if half else img.float()  # uint8 to fp16/32
                img /= 255.0  # 0 - 255 to 0.0 - 1.0
                if img.ndimension() == 3:
                    img = img.unsqueeze(0)
                t2 = time_sync()
                dt[0] += t2 - t1

                # Inference
                visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
                pred = model(img, augment=augment, visualize=visualize)
                t3 = time_sync()
                dt[1] += t3 - t2

                # Apply NMS
                pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
                dt[2] += time_sync() - t3

                # Process detections
                for i, det in enumerate(pred):  # detections per image
                    seen += 1
                    if webcam:  # batch_size >= 1
                        p, im0, _ = path[i], im0s[i].copy(), dataset.count
                        s += f'{i}: '
                    else:
                        p, im0, _ = path, im0s.copy(), getattr(dataset, 'frame', 0)

                    p = Path(p)  # to Path
                    save_path = str(save_dir / p.name)  # im.jpg, vid.mp4, ...
                    s += '%gx%g ' % img.shape[2:]  # print string

                    annotator = Annotator(im0, line_width=2, pil=not ascii)
                    w, h = im0.shape[1],im0.shape[0]
                    if det is not None and len(det):
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_coords(
                            img.shape[2:], det[:, :4], im0.shape).round()

                        # Print results
                        for c in det[:, -1].unique():
                            n = (det[:, -1] == c).sum()  # detections per class
                            s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                        xywhs = xyxy2xywh(det[:, 0:4])
                        confs = det[:, 4]
                        clss = det[:, 5]

                        # pass detections to deepsort
                        t4 = time_sync()
                        outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), im0)
                        t5 = time_sync()
                        dt[3] += t5 - t4

                        # draw boxes for visualization
                        if len(outputs) > 0:
                            for j, (output, conf) in enumerate(zip(outputs, confs)):

                                bboxes = output[0:4]
                                id = output[4]
                                cls = output[5]
                                #count
                                count_obj(bboxes,w,h,id)
                                c = int(cls)  # integer class
                                label = f'{id} {names[c]} {conf:.2f}'
                                annotator.box_label(bboxes, label, color=colors(c, True))

                                if save_txt:
                                    # to MOT format
                                    bbox_left = output[0]
                                    bbox_top = output[1]
                                    bbox_w = output[2] - output[0]
                                    bbox_h = output[3] - output[1]
                                    # Write MOT compliant results to file
                                    with open(txt_path, 'a') as f:
                                        f.write(('%g ' * 10 + '\n') % (frame_idx + 1, id, bbox_left,  # MOT format
                                                                    bbox_top, bbox_w, bbox_h, -1, -1, -1, -1))

                        LOGGER.info(f'{s}Done. YOLO:({t3 - t2:.3f}s), DeepSort:({t5 - t4:.3f}s)')

                    else:
                        deepsort.increment_ages()
                        LOGGER.info('No detections')

                    # Stream results
                    im0 = annotator.result()
                    if True:
                        global count
                        color=(255,0,0)
                        start_point = (0, h-350)
                        end_point = (w, h-350)
                        # To enable the line 
                        # cv2.line(im0, start_point, end_point, color, thickness=2)
                        cv2.line(im0, (0,0), (0,0), color, thickness=2)
                        thickness = 3
                        org = (150, 150)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 3
                        cv2.putText(im0, str(count), org, font, 
                        fontScale, color, thickness, cv2.LINE_AA)
                        endTime = datetime.datetime.utcnow()
                        # For every 4 seconds the count value is updated
                        #__lane 1__
                        if int((endTime - startTime).total_seconds()) > 10 :
                            # Here I have passed the thisLane as lane_1 but on connecting 4 cameras it must be variable
                            writeData(count,'lane_3')
                            count = 0
                            startTime = datetime.datetime.utcnow()
                        # Only on development the next three lines can be uncommented
                        cv2.imshow(str(p), im0)
                        if cv2.waitKey(1) == ord('q'):  # q to quit
                            raise StopIteration
                        #After debugging do comment the above three lines

 
 
                        
 
def writeData(count,thisLane):
    # Reading the existing data
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    jsonFile.close()
    # Modifying with our lane value
    # lane = "lane_1"
    data[f"{thisLane}"] = count
    # Updating with our lane value
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    jsonFile.close()
def count_obj(box,w,h,id):
    global count,data
    center_coordinates = (int(box[0]+(box[2]-box[0])/2) , int(box[1]+(box[3]-box[1])/2))
    if int(box[1]+(box[3]-box[1])/2) > (h -350):
        if  id not in data:
            count += 1
            data.append(id)
def generate_detection():
    with torch.no_grad():
        detect()
if __name__ == '__main__':
    generate_detection()








    
