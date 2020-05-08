# Betabot Localization and Navigation

- [Betabot Localization and Navigation](#betabot-localization-and-navigation)
  - [Project Description](#project-description)
  - [GUID](#guid)
  - [Project Rubric](#project-rubric)
  - [After you implement the pkg state your reflection below](#after-you-implement-the-pkg-state-your-reflection-below)
  - [Part I: Map (map_server)](#part-i-map-mapserver)
    - [In your own words how maps are represented in ROS?](#in-your-own-words-how-maps-are-represented-in-ros)
    - [State 5 algorithm for SLAM and the ROS implementation](#state-5-algorithm-for-slam-and-the-ros-implementation)
  - [Part II: Localization (amcl)](#part-ii-localization-amcl)
    - [In your own words how amcl works?](#in-your-own-words-how-amcl-works)
    - [Is there other better approaches to localize your robot rather than amcl?](#is-there-other-better-approaches-to-localize-your-robot-rather-than-amcl)
    - [What are the amcl limitations or the fail cases?](#what-are-the-amcl-limitations-or-the-fail-cases)
    - [Is amcl used in domain rather than Robotics?](#is-amcl-used-in-domain-rather-than-robotics)
  - [Part III: Navigation (move_base)](#part-iii-navigation-movebase)
    - [How many official local planner available in ROS?](#how-many-official-local-planner-available-in-ros)
    - [which local planner did you use?](#which-local-planner-did-you-use)
    - [In your own words how the local planner you selected works?](#in-your-own-words-how-the-local-planner-you-selected-works)
    - [How many official global planner available in ROS?](#how-many-official-global-planner-available-in-ros)
    - [which global planner did you use?](#which-global-planner-did-you-use)
    - [In your own words how the global planner you selected works?](#in-your-own-words-how-the-global-planner-you-selected-works)
    - [State your suggestion increase the overall performance?](#state-your-suggestion-increase-the-overall-performance)
    - [List the most time consuming problems you faced](#list-the-most-time-consuming-problems-you-faced)
    - [Demos](#demos)
    - [Screenshots](#screenshots)
      - [NAME:](#name)
      - [ID:](#id)

## Project Description 

Create a ROS package with custom launch files to localize the robot in an environment given the map and also to autonomous navigation. 

*Use the given [map](map/map2d.yaml) for the myoffice world [here](../betabot_gazebo/worlds/myoffice.world)* 

<p float="center">
  <img src="img/myoffice.png" width="589" /> 
  <img src="img/map2d.png" width="500" />
</p>


>NOTE: For the given map and a world the betabot robot should localize it self and move from currant pose to a given goal autonomously

## GUIDE
Follow where am I project from Udacity Software Robotics Engineer Nanodegree.

---
## Project Rubric

![rubric](img/reviews.jpg) 

---

## After you implement the pkg state your reflection below 
After implementing the project, I have gained knowledge about localization using amcl and know how to work with maps in ROS gazebo and RVIZ. 
---
## Part I: Map (map_server)

###  In your own words how maps are represented in ROS?
Maps are represented in ROS using two files:
1- .pgm file: which contains the map itself (The black and white pixels generated from packages such as pgm map creator or created manually using photo editing software as GIMP.)
2- .yaml file: the markup file that describes how this map is reflected on the gazebo world. It defines wieghts to the image resolution, hieght and width and other parameters that help localizing the map in the scence (World).
###  State 5 algorithm for SLAM and the ROS implementation

| SLAM Algorithm | ROS implementation |
|:--------------:|:------------------:|
|     GMapping   |      gmapping      |
| Acoustic SLAM  |                    |
|Audio-Visual SLAM|                    |
|Collaboratice SLAM|                    |
|                |                    |

---

## Part II: Localization (amcl)

### In your own words how amcl works?
AMCL is a localization algorithm which uses the concept of particle filters to localize a robot inside a given map. It takes input form laserscan and odom and tries to calculate if there is a shift (difference) between the tow. Through iterations, it tries to minimize this difference and thus reaching the destination and converges.
### Is there other better approaches to localize your robot rather than amcl?
As far as we know amcl is the best algorithm we can use to localize robots. It shows better performance than other localization algorithm such as Monte Carlo Localization (MCL).
### What are the amcl limitations or the fail cases?
1- It only uses laser scan to localize the robots, so if the laser fails to work, the robot will get stuck and won't be able to localize it self. Entegration of other sensor and input data such as GPS may solve this problem.
2- Particle filters approach are resources and time consuming specially if we have many objects in the world.
### Is amcl used in domain rather than Robotics?
It can be used for localization in any field rather than robotics such as in game developmet when we need to localize a game character in the map.
---

## Part III: Navigation (move_base)

### How many official local planner available in ROS?
There are may many local planners availabe for ROS such as dwa_local_planner, eband_local_planner, base_local_planner.
### which local planner did you use?
I use the base_local_planner.
### In your own words how the local planner you selected works?
It is working using particle filters as explained in the nanodegree.
### How many official global planner available in ROS?
For indigo, there are 3 gloabal planneers: global_planner, navfn, carrot_planner.
Reference: https://answers.ros.org/question/240812/what-global-planners-come-with-a-ros-indigo-installation/
### which global planner did you use?
navfn
### In your own words how the global planner you selected works?
It is working using particle filters as explained in the nanodegree.

---

### State your suggestion increase the overall performance?
If we have good resources we may increase the maximum number of particles used so that we acheive better accuracy.

### List the most time consuming problems you faced
1- First pgmmapcreator causes a lot of problems, but Eng. Abedlrhman provided us the map.
2- Changing parameters and variables that the nanodegree uses to work on our packages and maps also take sometime.
---

### Demos
Add unlisted youtube/drive videos

[Demo](https://drive.google.com/open?id=1xZ16IbL1hOIsS5MQbD5y6LCvolYkLyg3)

### Screenshots
1. rviz with all navigation launchers from turtulbot
2. gazebo

![image](<p float="center">
  <img src="img/screenshot.jpg" width="589" /> 
</p>)

---

#### NAME: Shady Atef Mohamed
#### ID: 201500841

---
