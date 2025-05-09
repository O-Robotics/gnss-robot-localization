# gnss-robot-localization
This is the dependent package: [robot_localization](https://github.com/cra-ros-pkg/robot_localization).

```
source /opt/ros/humble/setup.bash
sudo apt install ros-humble-robot-localization
sudo apt install \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-nav2-minimal-tb*
```
```
pip install -r requirements.txt
```


GNSS data needs to be published to the gnss_pose topic. 

Message type: `geometry_msgs/msg/PoseWithCovarianceStamped`.
