import cv2
import numpy as np
import open3d as o3d


mesh = o3d.io.read_triangle_mesh('/home/kaushik/PCD/cordless_drill_mesh.ply')
#text=cv2.imread('/home/gaurav/ocrtoc_materials/models/potted_meat_can/meshes/texture_map.png')

pcd = o3d.geometry.PointCloud()

pcd.points = mesh.vertices
pcd.colors = mesh.vertex_colors
pcd.normals = mesh.vertex_normals

o3d.visualization.draw_geometries([pcd])

o3d.io.write_point_cloud("/home/kaushik/PCD/cordless_drill_mesh.pcd", pcd)
print("Saved Point Cloud")
