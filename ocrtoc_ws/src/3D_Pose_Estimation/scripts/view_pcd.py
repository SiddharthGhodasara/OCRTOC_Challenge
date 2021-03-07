import open3d as o3d
import numpy as np 

pcd_file  = o3d.io.read_point_cloud("/home/kaushik/Documents/3D_vision/PCL_Tutorials/test_pcd.pcd")
print(pcd_file)
print(np.asarray(pcd_file.points))

o3d.visualization.draw_geometries([pcd_file],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
