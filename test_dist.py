import rospy
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import cv2
import numpy as np

class NavcamDistanceCalculator:
    def __init__(self):
        self.bridge = CvBridge()
        self.left_image = None
        self.right_image = None
        self.camera_info = None

        self.image_sub_left = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/image_raw', Image, self.left_image_callback)
        self.image_sub_right = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/right/image_raw', Image, self.right_image_callback)
        self.camera_info_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/camera_info', CameraInfo, self.camera_info_callback)

    def left_image_callback(self, data):
        self.left_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        self.calculate_distance()

    def right_image_callback(self, data):
        self.right_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        self.calculate_distance()

    def camera_info_callback(self, data):
        self.camera_info = data

    def calculate_distance(self):
        if self.left_image is None or self.right_image is None or self.camera_info is None :
            return

        # Calculate the distance and position for the left image
        left_distance, left_position = self.calculate_image_distance(self.left_image)

        # Calculate the distance and position for the right image
        right_distance, right_position = self.calculate_image_distance(self.right_image)

        if(right_distance < left_distance):
            print('right: ', right_distance)
        elif (right_distance == left_distance):
            print('center: ', left_distance)
        else:
            print('left: ', left_distance)
        
        # # Print the results
        # print('hello:\n')
        # rospy.loginfo('Distance to nearest object - Left: %f meters, position: %s, Right: %f meters, position: %s',
        #               left_distance, left_position, right_distance, right_position)

    def calculate_image_distance(self, image):
        # Convert the image to grayscale and blur it
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)

        # Threshold the image to create a binary image
        _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

        # Find the contours in the binary image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with the largest area
        if len(contours) > 0:
            contour = max(contours, key=cv2.contourArea)

            # Calculate the distance to the object
            fx = self.camera_info.K[0]
            baseline = 0.1 # Assume a baseline of 10 cm
            object_width = cv2.boundingRect(contour)[2]
            distance = fx * baseline / object_width

            # Calculate the position of the object relative to the center of the image
            image_center_x = self.camera_info.width / 2.0
            object_center_x = cv2.boundingRect(contour)[0] + object_width / 2.0
            position = 'left' if object_center_x < image_center_x else 'right'

            # Print the results
            # rospy.loginfo('Distance to nearest object: %f meters, position: %s', distance, position)

            # Show the image with the contour
            cv2.imshow(position, image)
            cv2.waitKey(1)

            return distance, position

        # If no contours were found, return None for distance and position
        return None, None

if __name__ == '__main__':
    rospy.init_node('navcam_distance_calculator')
    calculator = NavcamDistanceCalculator()
    rospy.spin()


# import rospy
# from sensor_msgs.msg import Image

# def callback(data):
#     print("Received an image message!")
#     print("Header:")
#     print(data.header)
#     print("Image dimensions:")
#     print("Width:", data.width)
#     print("Height:", data.height)
#     print("Encoding:", data.encoding)
#     print("Step:", data.step)

# if __name__ == '__main__':
#     rospy.init_node('image_attributes_printer', anonymous=True)
#     rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/image_raw', Image, callback)
#     rospy.spin()