# rfm_simulation

Simulation environment to test Robot Manager's ROS adaptor using a Turtlebot 2.

## Installation

Download the repository in your ROS workspace:

    cd <your_ros_ws>/src
    git clone https://github.com/ncs-robotmanager/rfm_simulation

Run the installer script:

     cd rfm_simulation
    ./installdep

Build your workspace:

    cd <your_ros_ws>
    catkin_make
    
## Simulation

Run the Turtlebot's simulation environment:

    roslaunch rfm_simulation simulation.launch

## Creating a new map

First run a minimal version of the simulation(without navigation stack):

    roslaunch rfm_simulation minimal_simulation.launch

Run the gmapping package and RVIZ:

    roslaunch rfm_simulation slam.launch

* Now you can use RVIZ to send a goal to the robot and create a map.

Once you're done mapping you, save the map by running:

    roscd rfm_simulation/maps
    rosrun map_server map_saver -f <name_of_map>

* Don't forget to update launch/navigate.launch with your newly created map.

