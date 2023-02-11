import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class CoordinateReporter(Node):

    def __init__(self):
        super().__init__('coord_reporter')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Unit coords: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    sw_unit = CoordinateReporter()

    rclpy.spin(sw_unit)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sw_unit.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()