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
        self.focal_length = None
        self.baseline = None

        self.Q = None
        self.left_map_x = None
        self.left_map_y = None
        self.right_map_x = None
        self.right_map_y = None
        
        self.image_sub_left = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/image_raw', Image, self.left_image_callback)
        self.image_sub_right = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/right/image_raw', Image, self.right_image_callback)
        self.camera_info_sub = rospy.Subscriber('/curiosity_mars_rover/camera_navcam/left/camera_info', CameraInfo, self.camera_info_callback)

    def left_image_callback(self, data):
        print('left img start')
        self.left_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        print('left check: right img ', self.right_image, 'cam ifno ', self.camera_info)
        if self.right_image is not None and self.camera_info is not None:
            depth = self.calculate_distance(self.left_image, self.right_image)
            print('Distance:', depth)
        print('left PLSSSSSSS')
        # cv2.imshow('Depth Image left', self.left_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # max_depth = self.left_image.max()
        # depth_img_scaled = self.left_image / max_depth
        # print('left max depth: ', max_depth)
        # print('left scale: ', depth_img_scaled)
        # # cv2.imwrite('depth_{}.raw'.format(count), self.left_image)
        # # self.calculate_distance()

    def right_image_callback(self, data):
        print('right img start')
        self.right_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        print('right check: left img ', self.left_image, 'cam ifno ', self.camera_info)
        if self.left_image is not None and self.camera_info is not None:
            depth = self.calculate_distance(self.left_image, self.right_image)
            print('Distance:', depth)
        print('right PLSSSSSS')
        # cv2.imshow('Depth Image right', self.right_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # max_depth = self.right_image.max()
        # depth_img_scaled = self.right_image / max_depth
        # print('right max depth: ', max_depth)
        # print('right scale: ', depth_img_scaled)
        # # cv2.imwrite('depth_{}.raw'.format(count), self.right_image)
        # # self.calculate_distance()

    def camera_info_callback(self, data):
        print('CAM INFO ')
        self.camera_info = data
        self.camera_info = data
        if self.focal_length is None:
            self.focal_length = data.K[0]
        if self.baseline is None:
            self.baseline = 0.42
        
        print('compy cam ifno')
        R1, R2, P1, P2, self.Q, roi1, roi2 = cv2.stereoRectify(cameraMatrix1=self.camera_info.K, cameraMatrix2=self.camera_info.K,
                                                        distCoeffs1=self.camera_info.D, distCoeffs2=self.camera_info.D,
                                                        imageSize=(self.camera_info.width, self.camera_info.height),
                                                        R=self.camera_info.R, T=np.array([self.baseline, 0, 0]))
        print('rectifying')
        # Generate rectification maps for each camera
        self.left_map_x, self.left_map_y, self.right_map_x, self.right_map_y = cv2.initUndistortRectifyMap(
            np.array(data.K).reshape((3, 3)), 
            np.array(data.D), 
            np.array(data.R).reshape((3, 3)), 
            np.array(data.P).reshape((3, 4))[:, :3],
            (data.width, data.height),
            cv2.CV_32FC1)
        print('yeay???')


    def calculate_distance(self, rect_left_img, rect_right_img):
        print('dist calc: basline ', self.baseline, 'focal ', self.focal_length, 'Q ', self.Q)
        if self.baseline is not None or self.focal_length is not None or self.Q is not None:
            # Compute the disparity map
            stereo = cv2.StereoBM_create(numDisparities=64, blockSize=11)
            disparity = stereo.compute(rect_left_img, rect_right_img)

            print('stereo ', stereo, 'disp ', disparity)
            
            # Compute the depth map
            depth = self.Q[2][3] / disparity
            print('d1', depth)
            depth = np.clip(depth, 0, 2**16 - 1)
            print('d2', depth)
            depth = depth.astype(np.uint16)
            print('d3', depth)

            # Compute the distance map
            depth = depth.astype(np.float32)
            print('d!!!', depth)
            dist_map = np.zeros(depth.shape, np.float32)
            print('dist map', dist_map)
            fx = np.float32(self.focal_length)
            print('focal', fx)
            baseline = np.float32(self.baseline)
            print('baseline', baseline)
            for y in range(dist_map.shape[0]):
                for x in range(dist_map.shape[1]):
                    if depth[y, x] > 0:
                        dist_map[y, x] = (fx * baseline) / depth[y, x]
            print('dist map filled', dist_map)            
            
            return dist_map


if __name__ == '__main__':
    rospy.init_node('navcam_distance_calculator')
    depth = NavcamDistanceCalculator()
    rospy.spin()
