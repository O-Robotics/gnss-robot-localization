from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[{
                'frequency': 10.0,  # match with gnss update freq
                'world_frame': 'map',
                'odom_frame': 'odom',
                'base_link_frame': 'base_link',
                'map_frame': 'map',
                
                'pose0': 'gnss_pose',
                'pose0_config': [True, True, True,   # X, Y, Z
                                False, False, False],  # do not use diretional data
                
                # adjust process noise based on GNSS covariance
                'process_noise_covariance': [
                    10.0, 0.0, 0.0, 0.0, 0.0, 0.0,   # X variance about 80-126
                    0.0, 10.0, 0.0, 0.0, 0.0, 0.0,   # Y 80
                    0.0, 0.0, 10.0, 0.0, 0.0, 0.0,   # Z 170
                    0.0, 0.0, 0.0, 0.1, 0.0, 0.0,   # Roll
                    0.0, 0.0, 0.0, 0.0, 0.1, 0.0,   # Pitch
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.1    # Yaw
                ],
                
                # iec（alignwith gnss initial precision）
                'initial_estimate_covariance': [
                    100.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 100.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 200.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.5, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.5, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.5
                ],
                
                'two_d_mode': False,  # keep 3d because it has altitude
                'transform_time_offset': 0.0,
                'transform_timeout': 0.0,
                'print_diagnostics': True,
                'debug': True  # to see details
            }],
            remappings=[
                ('odometry/filtered', 'odometry/global'),
                ('/set_pose', '/set_pose_ekf')
            ]
        )
    ])
