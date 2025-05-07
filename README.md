##### **DGMD E-17: Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence**
# Real-Time Visual Obstacle Detection on Duckiebot DB21J with NVIDIA Jetson Nano 4GB with GPU


## About
This project builds on the open-source Duckietown platform by deploying an autonomous robot with integrated object detection capabilities. It investigates how perception and control systems interact in real time, allowing the robot to identify and react to physical objects (represented by yellow rubber ducks) on the Duckietown road. The project emphasizes practical applications of computer vision and autonomous decision-making in a simplified yet dynamic setting.

## Instructions
The Duckiebot autonomously drives through a custom-built Duckietown layout, leveraging object detection to identify rubber ducks randomly positioned along the roadway. To enable this, we will collect training data from the Duckietown simulator and use it to train a YOLO (v5). This model will be integrated into Duckietown's autonomy stack.<br>
<img src="assets/duckiebot.jpg" alt="Duckiebot on track" width="150" height="150"/>

## Requirements
### Hardware ###
<ul>
  <li>Duckiebot DB21J with NVIDIA Jeson Nano 4GB</li>  
</ul>

### Accounts | Software ###
<ul><li>Duckietown account with valid token</li>
<li>Docker (installed and account set up)</li>
<li>Python (recommended: version 3.7 or higher)</li>
  <li>OpenCV - for computer vision and image processing</li>
  <li>YOLOv5 - for object detection and image recognition</li>
</ul>


## Setting up the Python virtual environment:
Building Duckiebot and 
Building instructions and manual 
Fork for the Duckietown GitHub repository
Create the environment:
```
python -m venv duckytown-venv
```
Activate the environment:
```
.\duckytown-venv\Scripts\activate
```
Install required packages:
```
pip install numpy
sudo apt-get install python3-pil python3-pil.imagetk
```
Deactivate the environment:
```
deactivate
```

