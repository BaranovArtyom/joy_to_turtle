from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    return LaunchDescription([

        # Launch turtlesim_node
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),

        # Launch your joy_to_turtle node
        Node(
            package='joy_to_turtle',
            executable='joy_to_turtle',
            name='joy_to_turtle_node'
        ),

    ])
