import rospy
import rosbag
from rosbridge_library.internal.publishers import rostopic

# Get the latest bag file
# bag_file = <path_to_latest_bag_file>

# Open the bag file
bag = rosbag.Bag(bag_file)

# Loop through the messages in the bag file
for topic, msg, t in bag.read_messages():
    # Convert the message to JSON format
    json_msg = rostopic.MessageToJson(msg)

    # Send the message over Rosbridge
    # Replace <rosbridge_topic> with the name of the topic you want to send the message to
    rostopic.publish_once('<rosbridge_topic>', json_msg)

# Close the bag file
bag.close()
