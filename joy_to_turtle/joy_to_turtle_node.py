import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyToTurtle(Node):
    def __init__(self):
        super().__init__('joy_to_turtle')
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def joy_callback(self, msg):
        twist = Twist()
        # Example: Map joystick axes to Twist message
        twist.linear.x = msg.axes[1]  # Assuming axis 1 is forward/backward
        twist.angular.z = msg.axes[0]  # Assuming axis 0 is left/right
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    joy_to_turtle = JoyToTurtle()
    rclpy.spin(joy_to_turtle)
    joy_to_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
