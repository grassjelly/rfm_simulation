# rfm_simulation

Simulation environment to test Robot Manager's ROS adaptor using a Turtlebot 2.

## Installation

1. Download the repository in your ROS workspace:

        cd <your_ros_ws>/src
        git clone https://github.com/ncs-robotmanager/rfm_simulation

2. Run the installer script:

        cd rfm_simulation
        ./installdep

3. Build your workspace:

        cd <your_ros_ws>
        catkin_make
    
## Simulation

Run the Turtlebot's simulation environment:

    roslaunch rfm_simulation simulation.launch

- Take note that loading the simulation environment during the first run may take a while.

## Creating a new map (optional)

This step is optional and only needed if you want to build a map for your new Gazebo environment. 

1. First, run a minimal version of the simulation(without navigation stack):

        roslaunch rfm_simulation minimal_simulation.launch

2. Run the gmapping package and RVIZ:

        roslaunch rfm_simulation slam.launch

* Now you can use RVIZ to send a goal to the robot and create a map.

3. Once you're done mapping you, save the map by running:

        roscd rfm_simulation/maps
        rosrun map_server map_saver -f <name_of_map>

* Remember to update [launch/navigate.launch](https://github.com/ncs-robotmanager/rfm_simulation/blob/master/launch/navigate.launch#L2) with your newly created map.

