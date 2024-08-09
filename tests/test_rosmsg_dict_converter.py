import unittest
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import String, Header
from sensor_msgs.msg import Image
from rosmsg_dict_converter.converter import (
    ros_message_to_dict,
    dict_to_ros_message,
    a_dict_to_ros_message,
)


class TestRosMsgDictConverter(unittest.TestCase):
    def test_rosmsg_to_dict_std_msgs(self):
        string_msg = String(data="hello")
        string_dict = ros_message_to_dict(string_msg)
        self.assertEqual(string_dict, {"data": "hello"})

        header_msg = Header(seq=1, stamp=None, frame_id="base_link")
        header_dict = ros_message_to_dict(header_msg)
        self.assertEqual(header_dict["seq"], 1)
        self.assertEqual(header_dict["frame_id"], "base_link")

    def test_rosmsg_to_dict_geometry_msgs(self):
        pose_msg = Pose(
            position=Point(x=1.0, y=2.0, z=3.0),
            orientation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0),
        )
        pose_dict = ros_message_to_dict(pose_msg)
        self.assertEqual(pose_dict["position"]["x"], 1.0)
        self.assertEqual(pose_dict["orientation"]["w"], 1.0)

    def test_rosmsg_to_dict_sensor_msgs(self):
        image_msg = Image(width=640, height=480, encoding="rgb8")
        image_dict = ros_message_to_dict(image_msg)
        self.assertEqual(image_dict["width"], 640)
        self.assertEqual(image_dict["height"], 480)
        self.assertEqual(image_dict["encoding"], "rgb8")

    def test_dict_to_rosmsg_std_msgs(self):
        string_dict = {"data": "hello"}
        string_msg = dict_to_ros_message("std_msgs/String", string_dict)
        self.assertEqual(string_msg.data, "hello")

        header_dict = {"seq": 1, "frame_id": "base_link"}
        header_msg = dict_to_ros_message("std_msgs/Header", header_dict)
        self.assertEqual(header_msg.seq, 1)
        self.assertEqual(header_msg.frame_id, "base_link")

    def test_dict_to_rosmsg_geometry_msgs(self):
        pose_dict = {
            "position": {"x": 1.0, "y": 2.0, "z": 3.0},
            "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0},
        }
        pose_msg = dict_to_ros_message("geometry_msgs/Pose", pose_dict)
        self.assertEqual(pose_msg.position.x, 1.0)
        self.assertEqual(pose_msg.orientation.w, 1.0)

    def test_dict_to_rosmsg_sensor_msgs(self):
        image_dict = {"width": 640, "height": 480, "encoding": "rgb8"}
        image_msg = dict_to_ros_message("sensor_msgs/Image", image_dict)
        self.assertEqual(image_msg.width, 640)
        self.assertEqual(image_msg.height, 480)
        self.assertEqual(image_msg.encoding, "rgb8")

    def test_a_dict_to_rosmsg(self):
        point_msg = Point(x=1.0)
        point_dict = {"y": 2.0}
        updated_point_msg = a_dict_to_ros_message(point_msg, point_dict)
        self.assertEqual(updated_point_msg.x, 1.0)
        self.assertEqual(updated_point_msg.y, 2.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
