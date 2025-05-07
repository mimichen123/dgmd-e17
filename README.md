##### **DGMD E-17: Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence**
---
# Real-Time Visual Obstacle Detection on Duckiebot DB21-J4 with NVIDIA Jetson Nano 4GB


## About
This project builds on the open-source Duckietown platform by deploying an autonomous robot with object detection capabilities. It investigates how perception and control systems interact in real time, allowing the robot to identify and react to physical objects (represented by yellow rubber ducks) on the Duckietown road. The project emphasizes practical applications of computer vision and autonomous decision-making in a simplified yet dynamic setting.

## Background
The Duckiebot autonomously drives through a custom-built Duckietown layout, leveraging object detection to identify rubber ducks randomly positioned along the roadway. To support this functionality, we collect training data from the Duckietown simulator and use it to train a YOLOv5 object detection model. Once trained, the model will be integrated into the Duckietown autonomy stack to enhance the robot’s perception capabilities in real time.<br><br>
<img src="assets/duckiebot.jpg" alt="Duckiebot on track" width="150" height="150"/>

## Requirements
### Hardware ###
<ul>
  <li>Duckiebot DB21-J4 with NVIDIA Jeson Nano 4GB</li>  
</ul>

### Accounts | Software ###
<ul><li>Duckietown account with valid token (use dts1 not dts2)</li>
  <li>Duckietown shell command installed</li>
<li>Docker (installed and account set up)</li>
<li>Python (recommended: version 3.7 or higher)</li>
  <li>OpenCV - for computer vision and image processing</li>
  <li>YOLOv5 - for object detection and image recognition</li>
</ul>

## License
This repository inherits the same license as the original <a href="https://github.com/duckietown/duckietown-lx">Duckietown LX</a> repository.
For full details on the licensing terms, please refer to the original repository.

## Instructions

<ol>
  <li>
    The Duckietown Learning Experience<br>
    <ul style="list-style-type: disc;"><li>
    Once your Duckiebot is built, fork the 
    <a href="https://github.com/duckietown/duckietown-lx">Duckietown-LX learning environment repository</a> and follow the setup steps.
  </li>
    <li>The purpose of this fork is to add and test our solutions to the original Duckietown Learning Experiences repository.</li></ul>
      <br></li>
    
  <li>Create your own GitHub repository<br>
    Setup your own GitHub repository to store and track this solution and make edits. 
  </li><br>
  
  <li>
  Update your systems<br>
  Before proceeding, update all system packages, dependencies, shell, laptop/desktop, and the Duckiebot to ensure compatibility.<br><br>  
  <pre><code>dts update
dts desktop update
dts duckiebot update [your_robot_name]</code></pre>
</li>
  </ol>
  
  ## Integrate your solution into the Duckietown autonomy stack<br>
  To integrate your work, follow the steps below in your local duckietown-lx environment.
  
  ### 📦  Object Detection ###
  Copy the implementation files to the following directory: <code>object-detection/packages/solution</code><br>
  <ul>    
    <li><a href="object-detection/dt_object_detection_training.ipynb">Object detection training</a>  – Google Colab notebook for model training</li>
    <li><a href="object-detection/integration_activity.py">Object detection integration</a> - handles integration logic</li>
  </ul>
  
  ### 🛣️  Lane Following ###
  Copy the implementation files to the following directory: <code>visual-lane-servoing/packages/solution</code><br>  
  <ul>    
    <li><a href="lane-following/visual_servoing_activity.py"">Visual Lane Servoing</a> - main lane following logic</li>
  </ul>
<br><br>

## 🚀 Deploy and Test on Duckiebot ##

#### Pull the latest changes from the solution branch<br>   
  If you have already cloned the repository and copied the solution files, and you want to update your local copy with the latest changes, run the following command in your Duckietown shell:<br><br>
  <pre><code>git pull origin [branch-name]</code></pre>

#### Run a local evaluation to check for code errors
```
dts code evaluate
```
#### Execute Solution on Duckiebot
```
dts code workbench --duckiebot [your_robot_name]
```
#### Run Duckiebot Joystick Controller<br>
<ol><li>Open a new terminal window.</li><br>
<li>Launch the Duckiebot joystick controller by running</li>  
</ol>	

```
dts duckiebot keyboard_control ![your_robot_name]
```
### 📦  Object Detection ### 
<ol><li>Use the joystick controller to start navigating the Duckiebot</li><br>
	<li>As the Duckiebot moves, its onboard camera should detect and identify rubber duckies positioned along the road</li>
</ol>

### 🛣️  Lane Following ###
<ol><li>Click Calibrate to perform sensor and camera calibration</li><br>
<li>Click start to begin lane-following behavior</li><br>
<li>Click Stop to stop the robot</li></ol>

___ 
## Troubleshooting
<ul>
  <li>
    Make sure you are logged into Docker using <code>dts</code><br><br>
    <pre><code>dts challenges config --docker-username &lt;USERNAME&gt; --docker-password &lt;PASSWORD&gt;</code></pre>
  </li>
  <li>
    If you are getting errors, check that you are using a <code>dts1</code> token and not a <code>dts2</code> token.
  </li>
</ul>
