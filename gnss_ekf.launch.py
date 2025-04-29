from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gnss_ekf',
            executable='gnss2pose',
            name='gnss_to_pose',
            output='screen'
        ),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[{
                'frequency': 10.0,
                'world_frame': 'map',
                'odom_frame': 'odom',
                'base_link_frame': 'base_link',
                'map_frame': 'map',
                'pose0': 'gnss_pose',
                'pose0_config': [True, True, True, False, False, False],
                'process_noise_covariance': [
                    10.0, 0, 0, 0, 0, 0,
                    0, 10.0, 0, 0, 0, 0,
                    0, 0, 10.0, 0, 0, 0,
                    0, 0, 0, 0.1, 0, 0,
                    0, 0, 0, 0, 0.1, 0,
                    0, 0, 0, 0, 0, 0.1
                ],
                'initial_estimate_covariance': [
                    100.0, 0, 0, 0, 0, 0,
                    0, 100.0, 0, 0, 0, 0,
                    0, 0, 200.0, 0, 0, 0,
                    0, 0, 0, 0.5, 0, 0,
                    0, 0, 0, 0, 0.5, 0,
                    0, 0, 0, 0, 0, 0.5
                ],
                'two_d_mode': False,
                'transform_time_offset': 0.0,
                'transform_timeout': 0.0,
                'print_diagnostics': True,
                'debug': True
            }],
            remappings=[
                ('odometry/filtered', 'odometry/global'),
                ('/set_pose', '/set_pose_ekf')
            ]
        )
    ])
