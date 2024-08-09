from rich.console import Console
from rosmsg_dict_converter.converter import (
    ros_message_to_dict,
    dict_to_ros_message,
    a_dict_to_ros_message,
)

from geometry_msgs.msg import Pose, PoseArray, Point

console = Console()

# ----------------------------
# ros message to dict
pose = Pose()
pose_dict = ros_message_to_dict(pose)
console.print(f"{pose_dict=}")

# dict to ros message
pose_dict = {
    "position": {"x": 0.0, "y": 0.0, "z": 0.0},
    "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 0.0},
}
pose = dict_to_ros_message("geometry_msgs/Pose", pose_dict)
console.print(f"{pose=}")

# ----------------------------
# Even the message has a list field without value, it can be converted to dict
pose_array = PoseArray()
pose_array_dict = ros_message_to_dict(pose_array, include_defaults=True)
console.print(f"{pose_array_dict=}")

pose_array_dict = {
    "header": {"seq": 0, "stamp": {"secs": 0, "nsecs": 0}, "frame_id": ""},
    "poses": [
        {
            "position": {"x": 1.0, "y": 0.0, "z": 0.0},
            "orientation": {"x": 1.0, "y": 0.0, "z": 0.0, "w": 0.0},
        }
    ],
}

pose_array = dict_to_ros_message("geometry_msgs/PoseArray", pose_array_dict)
console.print(f"{pose_array=}")

# ----------------------------
# if you want to keep the part of the value of the ros msg
# use `a_dict_to_ros_message` instead of `dict_to_ros_message`

point = Point()
point.x = 1.0

point_dict = ros_message_to_dict(point)
point_dict["y"] = 2.0

# the value of point.x is still 1.0
point = a_dict_to_ros_message(point, point_dict)
console.print(f"{point=}")
