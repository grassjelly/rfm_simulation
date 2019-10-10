cmake_minimum_required(VERSION 2.8.3)
project(rfm_simulation)

find_package(catkin REQUIRED COMPONENTS roslaunch)

catkin_package()

roslaunch_add_file_check(launch/minimal_simulation.launch)
roslaunch_add_file_check(launch/simulation.launch)