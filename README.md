##### **DGMD E-17: Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence**
# Real-Time Visual Obstacle Detection on Duckiebot DB21-J4 with NVIDIA Jetson Nano 4GB with GPU


## About
This project builds on the open-source Duckietown platform by deploying an autonomous robot with integrated object detection capabilities. It investigates how perception and control systems interact in real time, allowing the robot to identify and react to physical objects (represented by yellow rubber ducks) on the Duckietown road. The project emphasizes practical applications of computer vision and autonomous decision-making in a simplified yet dynamic setting.

## Instructions
The Duckiebot autonomously drives through a custom-built Duckietown layout, leveraging object detection to identify rubber ducks randomly positioned along the roadway. To enable this, we will collect training data from the Duckietown simulator and use it to train a YOLO (v5). This model will be integrated into Duckietown's autonomy stack.<br>
<img src="assets/duckiebot.jpg" alt="Duckiebot on track" width="150" height="150"/>

## Requirements
### Hardware ###
<ul>
  <li>Duckiebot DB21-J4 with NVIDIA Jeson Nano 4GB</li>  
</ul>

### Accounts | Software ###
<ul><li>Duckietown account with valid token</li>
  <li>Duckietown Shell command installed</li>
<li>Docker (installed and account set up)</li>
<li>Python (recommended: version 3.7 or higher)</li>
  <li>OpenCV - for computer vision and image processing</li>
  <li>YOLOv5 - for object detection and image recognition</li>
</ul>


## Setting up the Duckietown learning environment:

Make sure system is up-to-date
```
dts duckiebot update [your robot name]
```
Fork the [duckietown-lx repository](https://github.com/duckietown/duckietown-lx)
Clone the repository (replace with your GitHub username):
```
git clone -b mooc2022 git@github.com:<your_username>/duckietown-lx
```
Change directory to duckietown-lx
```
cd duckietown-lx
```
Setup this repository to sync with your fork
```
git remote -v
```
Specify new remote upstream repository
```
git remote add upstream https://github.com/duckietown/duckietown-lx```
```



