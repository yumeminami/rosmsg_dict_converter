# rosmsg_dict_converter

## Description

This package provides a tool to convert a ROS message dictionary to a Python dictionary and vice versa.

## Features

- Convert a ROS message dictionary to a Python dictionary
- Convert a Python dictionary to a ROS message dictionary
- Allow populate empty lists with default values for the message types.
- Also allows passing an existing message to update its fields with values from the dictionary.

## Installation

```bash
pip install rosmsg_dict_converter
```

## Usage

1. ros_message_to_dict

```python
from rosmsg_dict_converter.converver import ros_message_to_dict

from geometry_msgs.msg import Pose

# ros message to dict
pose = Pose()
pose_dict = ros_message_to_dict(pose)
```

2. dict_to_ros_message

```python
from rosmsg_dict_converter.converver import dict_to_ros_message

from geometry_msgs.msg import Pose

# dict to ros message
pose_dict = {
    'position': {
        'x': 1.0,
        'y': 2.0,
        'z': 3.0
    },
    'orientation': {
        'x': 0.0,
        'y': 0.0,
        'z': 0.0,
        'w': 1.0
    }
}
pose = dict_to_ros_message("geometry_msgs/Pose", pose_dict)
```

3. populate_empty_lists

```python
from rosmsg_dict_converter.converver import ros_message_to_dict,

from geometry_msgs.msg import PoseArray

# ros message to dict
pose_array = PoseArray()
pose_array_dict = ros_message_to_dict(pose_array, include_defaults=True)
# output
# pose_array_dict={'header': {'seq': 0, 'stamp': {'secs': 0, 'nsecs': 0}, 'frame_id': ''}, 'poses': [{'position': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0}}]}
```

4. update_ros_message

```python
from rosmsg_dict_converter.converver import a_dict_to_ros_message,ros_message_to_dict
from geometry_msgs.msg import Point

point = Point()
point.x = 1.0

point_dict = ros_message_to_dict(point)
point_dict["y"] = 2.0

# the value of point.x is still 1.0
point = a_dict_to_ros_message(point, point_dict)
console.print(f"{point=}")

# output
# point=Point(x=1.0, y=2.0, z=0.0)
```

## License

[Apache License 2.0](LICENSE)