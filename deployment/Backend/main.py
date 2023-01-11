import subprocess

process1 = subprocess.Popen(["python", "l1.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "l2.py"])
process3 = subprocess.Popen(["python", "l3.py"])
process4 = subprocess.Popen(["python", "l4.py"])
process5 = subprocess.Popen(["python", "writeDatabase.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()
process4.wait()
process5.wait()