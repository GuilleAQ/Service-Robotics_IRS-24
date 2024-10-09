# Localized Vacuum Cleaner

<div align="center">
<img width=600px src="https://github.com/GuilleAQ/Service-Robotics_IRS-24/blob/main/P1/resources/figures/1.png" alt="explode"></a> 
</div>

<h3 align="center"> Localized Vacuum Cleaner </h3>

<div align="center">
<img width=100px src="https://img.shields.io/badge/status-finished-brightgreen" alt="explode"></a>
<img width=100px src="https://img.shields.io/badge/license-Apache-orange" alt="explode"></a>
</div>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Task description](#Task-description)
- [Robot API](#Robot-API)
- [Coordinate to Pixel Conversion](#Coordinate-to-Pixel-Conversion)


## Task description
The objective of this practice is to implement the logic of a navigation algorithm for an autonomous vacuum cleaner by making use of the location of the robot.
The robot is equipped with a map and knows it’s current location in it. The main objective will be to cover the largest area of ​​a house using the programmed algorithm.

## Robot API
- import HAL - to import the HAL(Hardware Abstraction Layer) library class. This class contains the functions that sends and receives information to and from the Hardware(Gazebo).
- import GUI - to import the GUI(Graphical User Interface) library class. This class contains the functions used to view the debugging information, like image widgets.
- HAL.setV() - to set the linear speed
- HAL.setW() - to set the angular velocity
- HAL.getPose3d().x - to get the X coordinate of the robot
- HAL.getPose3d().y - to get the Y coordinate of the robot
- HAL.getPose3d().yaw - to get the orientation of the robot
- HAL.getBumperData().state - To establish if the robot has crashed or not. Returns a 1 if the robot collides and a 0 if it has not crashed.
- HAL.getBumperData().bumper - If the robot has crashed, it turns to 1 when the crash occurs at the center of the robot, 0 when it occurs at its right and 2 if the collision is at its left.
- HAL.getLaserData() - It allows to obtain the data of the laser sensor, which consists of 180 pairs of values ​​(0-180º, distance in meters).
- GUI.showNumpy(mat) - Displays the matrix sent. Accepts an uint8 numpy matrix, values ranging from 0 to 127 for grayscale and values 128 to 134 for predetermined colors
(128 = red; 129 = orange; 130 = yellow; 131 = green; 132 = blue; 133 = indigo; 134 = violet). Matrix should be square and the dimensions bigger than 100*100 for correct visualization.
Dimensions bigger than 1000*1000 may affect performance.

## Coordinate to Pixel Conversion
To do this, I will create a Python program where I provide an image (in this case 1012x1013 pixels), and by clicking on different points of the image, it will return the coordinates of
the pixels where I clicked. Additionally, using the functions of the [API](#Robot-API), I will obtain the world coordinates in Gazebo.

In the following images, you can see how clicking on the map image returns the coordinates of the pixels where the click is made.

<div align="center">
<img width=600px src="https://github.com/GuilleAQ/Service-Robotics_IRS-24/blob/main/P1/resources/figures/click1.png" alt="explode"></a> 
</div>

<div align="center">
<img width=600px src="https://github.com/GuilleAQ/Service-Robotics_IRS-24/blob/main/P1/resources/figures/click2.png" alt="explode"></a> 
</div>

Now, following the theory, we know that we need to solve the equations:
<div align="center">
<img width=600px src="https://github.com/GuilleAQ/Service-Robotics_IRS-24/blob/main/P1/resources/figures/8.png" alt="explode"></a> 
</div>

For this, I have created another Python code that calculates an affine transformation (rotation, scale, and translation) that maps pixel coordinates from an image to coordinates in the Gazebo world. 
It uses a set of known points in both reference systems (pixels and Gazebo world) to estimate the transformation parameters.

Since I have already taken the points in pixels and Gazebo coordinates (in total, I have made 10 measurements), I can obtain the rotation, translation, and scale parameters.

```python
pixel_coords = [
    (59, 74),
    (369, 82),
    (421, 627),
    (273, 685),
    (481, 329),
    (955, 318),
    (790, 775),
    (826, 961),
    (188, 863),
    (59, 967)
]
```

```python
world_coords = [
    (5.07, -3.27),
    (2.06, -3.10),
    (1.49, 2.11),
    (2.94, 2.56),
    (0.93, -0.82),
    (-3.62, -0.84),
    (-2.1, 3.55),
    (-2.44, -5.34),
    (3.84, 4.52),
    (5.07, 5.52)
]
```

The obtanined results:

<div align="center">
<img width=600px src="https://github.com/GuilleAQ/Service-Robotics_IRS-24/blob/main/P1/resources/figures/9.png" alt="explode"></a> 
</div>


