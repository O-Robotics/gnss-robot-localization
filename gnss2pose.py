import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PoseWithCovarianceStamped
import utm  # pyproj or utm

class GnssToPose(Node):
    def __init__(self):
        super().__init__('gnss_to_pose')
        self.subscription = self.create_subscription(
            NavSatFix,
            '/fix',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(
            PoseWithCovarianceStamped,
            'gnss_pose',
            10)
        # store first location as orgin
        self.origin = None
        
    def listener_callback(self, msg):
        if msg.status.status < 0:  # no valid gnss data
            return
            
        pose_msg = PoseWithCovarianceStamped()
        pose_msg.header = msg.header
        pose_msg.header.frame_id = 'map'  # Set to map coordinate
        
        # transform to UTM
        utm_data = utm.from_latlon(msg.latitude, msg.longitude)
        
        # Set the origin (first valid point)
        if self.origin is None:
            self.origin = (utm_data[0], utm_data[1], msg.altitude)
            self.get_logger().info(f"Set origin to: {self.origin}")
        
        # Calculate the position relative to the origin
        pose_msg.pose.pose.position.x = utm_data[0] - self.origin[0]
        pose_msg.pose.pose.position.y = utm_data[1] - self.origin[1]
        pose_msg.pose.pose.position.z = msg.altitude - self.origin[2]
        
        # Extract the covariance matrix from the message and restructure it into 6x6 format
        # NavSatFix uses 3x3 position covariance, we need to map it to 6x6 covariance of the Pose message
        pose_msg.pose.covariance = [
            msg.position_covariance[0], msg.position_covariance[1], msg.position_covariance[2], 0.0, 0.0, 0.0,
            msg.position_covariance[3], msg.position_covariance[4], msg.position_covariance[5], 0.0, 0.0, 0.0,
            msg.position_covariance[6], msg.position_covariance[7], msg.position_covariance[8], 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 1.0, 0.0, 0.0,  # Directional covariance (large values ​​indicate uncertainty)
            0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 1.0
        ]
        
        self.publisher.publish(pose_msg)

def main(args=None):
    rclpy.init(args=args)
    node = GnssToPose()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
