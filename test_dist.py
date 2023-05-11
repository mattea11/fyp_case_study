
# import rospy
# import open3d as o3d
# import ros_numpy
# import numpy as np
# from sensor_msgs.msg import PointCloud2
# import sensor_msgs.point_cloud2 as pc2
# # from std_msgs.msg import Header

# def point_cloud_callback(msg):
#     # Convert PointCloud2 message to Numpy array
#     points = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(msg)
#     print('points: ', points)

#     # Convert Numpy array to Open3D point cloud
#     cloud = o3d.geometry.PointCloud()
#     cloud.points = o3d.utility.Vector3dVector(points)

#     print('cloud points: ', np.asarray(cloud.points))

#     # Apply voxel grid filtering to remove noise
#     min_bound = np.min(points, axis=0)
#     max_bound = np.max(points, axis=0)
#     cloud_downsampled, voxel_ind, _ = cloud.voxel_down_sample_and_trace(voxel_size=0.01, min_bound=min_bound, max_bound=max_bound)
#     print('cloud samp: ', cloud_downsampled)
#     print('voxel ind: ', voxel_ind)

#     # Apply Euclidean clustering to segment point cloud into clusters
#     labels = np.array(cloud_downsampled.cluster_dbscan(eps=0.3, min_points=10, print_progress=False))
#     print('labels: ', labels)

#     # Calculate the distance to each cluster and print it to the terminal
#     for i in np.unique(labels):
#         # if i == -1:  # Skip noise points labeled as -1
#         #     continue
#         print('i: ', i)
#         print('points: ', points.shape)
#         cluster_mask = labels == i
#         print('clust mask: ', cluster_mask.shape)
#         cluster_points = points[cluster_mask]
#         cluster_centroid = np.mean(cluster_points, axis=0)[:3]
#         distance = np.linalg.norm(cluster_centroid)
#         print(f"Distance to cluster {i}: {distance:.2f} meters")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan

def get_latest_distance():
    rospy.init_node('rover_distance_node')
    data = rospy.wait_for_message('/merged_scan', LaserScan)

    dist = data.ranges#
    smallest = min(dist)
    # dist = f"{dist:.3f}"
    print(dist)
    print(smallest)

    # my_dict = {'curr_distances': dist}
    # json_speed = json.dumps(my_dict)
    # return json_speed


if __name__ == '__main__':
    
    get_latest_distance()

    rospy.spin()
