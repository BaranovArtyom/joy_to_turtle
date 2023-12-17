sudo apt-get install ros-<rosdistro>-teleop-twist-joy

. /opt/ros/<rosdistro>/setup.bash

ros2 run turtlesim turtlesim_node

ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'

colcon build --packages-select joy_to_turtle
. install/setup.bash
ros2 run joy_to_turtle joy_to_turtle

*********************************************

colcon build
ros2 launch joy_to_turtle joy_to_turtle.launch.py
