
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy_to_turtle',
            executable='joy_to_turtle',
            name='joy_to_turtle_node',
            output='screen',
        )
    ])
