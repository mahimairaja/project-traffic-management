<p align="center">
  <a href="" rel="noopener">
 <img width=600px height=200px src="assets/logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Traffic Analysis and Management</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center" style="padding-left : 50px;padding-right : 50px;">
“Information is the oil of the 21st century, and analytics is the combustion engine.”
</p>
    <br> 


## 📝 Table of Contents

- [About](#about)
- [Sample Output](#output)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Future Vision](#future)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The project demostrates the implementation of web-based analysis on a edge computing system with a deep neural model running on it that can help us to undertand the pattern of traffic in that particular area. By the data collected by our algorithm we can significantly optimise the waiting time of vehicles in the traffic lanes.

## ⭐︎ My Contributions :
- Backend - Flask and Jinja ( Python )
- Front-end - J-query ( Data retrieval using AJAX ) 
- Database - Firebase ( No-SQL ) in cloud , Sqlite ( RDBMS ) in edge

## ✅ Sample Output <a name = "output"></a>
### Traffic density : 
<img src=assets/density.gif>
<br><br>

### Real-Time Graph : 
<img src=assets/graph.gif>
<br><br>

### Local Database (RDBMS) : 
<img src=assets/database.gif>
<br><br>


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

- As we use deep learning  model make sure you have enough computing power and good GPU for better results.
- It is good to have CUDA installed.


### Installing


``` bash
git clone https://github.com/mahimai-raja/project-traffic-control.git

cd project-traffic-control
pip install requirements.txt
```

## 🔧 Running the program <a name = "tests"></a>

``` bash
cd deployment
```
### Run the back-end

This script script run four cameras and collect datafrom the video sensors and enter them into the databases. Untill we interrupt the backend keeps it alive forever.

```bash
cd backend
python main.py
```

### Run the Front-end

Before running the flask app set the flask environment variable.

```bash
cd ..
export FLASK_APP=main  # This is for mac ( Check for your OS )
python -m flask run
```

## 🎈 Usage <a name="usage"></a>

- On the website home page you can see a real-time graph and density by the vehicle count in that signal.
- The graph helps to identify the traffic pattern along the time.
- The color code mechanism helps us to understand the intensity of the traffic comparitatively.

## 🚀 Deployment <a name = "deployment"></a>

As we use light framework like flask and Yolo nano, this site can be deployed on an edge computing system of your favorite easily.

## ⛏️ Built Using <a name = "built_using"></a>

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Server Framework
- [firebase](http://firebase.google.com/) - Database
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Python Web scripts
- [Jquery](https://jquery.com) - Front-end framework
- [Yolov5](https://github.com/ultralytics/yolov5) - Detection algorithm
<br><br>

## 👨‍💻 Future Vision  <a name = "future"></a>
<details>
<summary>socket.io instead of REST 
</summary>

```
Instead of JQuery API (HTTP)  calls for live chart, sockets can be implemented.
```
</details>
<details>
<summary>Updated CV Architecture </summary>

```
Since YoloV5 is bit older algorithm, an upto-date light weight algorithms can be integrated. 
```
</details>
<details>
<summary>Fuzzy Logic Model
</summary>

```
Currently the signal lights are manually controlled by the traffic officer. But in feature I suggest an neural fuzzy logic model can automate the task.
```
</details>

<details>
<summary>Federated Learning
</summary>

```
To implement federated learning for continous updatation of the model with privacy.
```
</details>
<br>


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Honourable [Dr.Getzi Jeba]() mam has guided the project from the beginning to the end.
- The detection algorithm is inspired from YoloV5 and DeepSort.

## ✍️ Authors <a name = "authors"></a>

- [Mahimai Raja J](https://github.com/mahimai-raja) 
- [Saran](#) 
- [Karan](#) 
- [Jemmimah](#) 
- [Praveena](#)