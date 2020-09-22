# OCRTOC_Challenge

## To Do: 

1. Test on muliple scenes and find common modes of failure 
2. Optimize grasping for elliptical box and pudding box 
3. Feedback in the algo & Recovery behaviour: If it hasn't grasped an object and placed it, don't move on to the next object. 
4. Figure out why master_chef_can's search region is getting messed up 
5. PC Registration 
6. Compensate for the differences between grasp center and geometric center
7. Retrain YOLO from all simulation scenes (take screenshots) and label 
8. Error checking at the end of each run for 6D poses 


For later: 

1. How do you find free space in the scene dynamically? OUTPUT: Occupancy grid  

- Use kinect or realsense to find depth and set threshold beyond which the table can be considered free 
- Extract the segmented Pointcloud and any region not belonging to this PC would be considered as free 
- Get dimensions of objects from target.world and width and length from yolo to calculate free space
- From gazebo, extract points of contact using which we could construct a bounding box of occupancy and free space (only sim)
- Make an occupancy grid using the above information for future path planning requirements 


2. Simplify scene approach (approach 1) 


- Feedback from gazebo contacts (with table) to see if it actually lies on table 
- Update the occupancy grid after each simplication maneuver 
- Run object detection on all possible objects in the current scene extract their target locations in the world file
- Only place it in the goal location if it need not be placed on top of another object
-Make all objects lie on table 

3. Priority approach (approach 2) 

- Perform (5) and focus on only one pile ignoring all other objects  
- To free up target location: 
	-Use a combination of grasping and sliding to nudge unwanted objects away 
	-Grasp and place in a temporary location 
- Repeat for other piles until no other piles are detected 


4. Heuristic that decides whether to use grasping or sliding (applicable to both approaches)

- Grasp feasibility matrix for all objects in the scene
- Use slide maneuver for all objects that have the least score in the grasp feasibilty table until graspable 
- Dynamically disable gazebo grasp plugin if sliding is chosen by heuristic for grasping
- Path planning with collision avoidance to move to the object to the edge of the table for improving grasp feasibility 
	- Exhausts all options to reach edge of the table without encountering any collisions 
	- If there no such path, find a path that involves removing the least amount of objects to reach the edge of the table 


5. Read world file and find the stacking order  - refinement of exiting method. Assign priorities



## Assumptions: 

1. Robustness of the object detector, grasp detector (BIG PROBLEM), accuracy of the target world files 


## Failure Log: 

1. Elliptical box grasp failure: Orientation given by haf grasping was good 
2. Jenga box graped towards the end, causing problems \
3. Master chef can not detected in 1-2 : Retrain yolo
4. Master chef can detected as jenga box: Retrain yolo
