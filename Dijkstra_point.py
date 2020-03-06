from dijkstra import *
import sys

start_coord_row = int(input("Enter the starting row coordinates of the node(1-200):  "))
start_coord_column = int(input("Enter the starting column coordinates of the node(1-300):  ")) 
goal_coord_row = int(input("Enter the starting goal node row coordintes(1-200):  "))
goal_coord_column = int(input("Enter the starting goal node column coordinates(1-300):  "))
radius = 0
clearance = 0
        
start_coord = (start_coord_row,start_coord_column)
goal_coord = (goal_coord_row, goal_coord_column)
        
dijkstra = Node(start_coord,goal_coord,radius,clearance)
        
if(dijkstra.validMove(start_coord[0],start_coord[1]) == True and dijkstra.validMove(goal_coord[0],goal_coord[1]) == True and dijkstra.ObstacleDetection(start_coord[0],start_coord[1]) == False and dijkstra.ObstacleDetection(goal_coord[0],goal_coord[1]) == False):


    (distance_from_start_to_goal, backtrack_states, explored_states) = dijkstra.dijkstra()
    print(len(backtrack_states))
    dijkstra.pathAnimation(explored_states, backtrack_states, "./dijkstra_simulation.avi")

    # print optimal path found or not
    if(distance_from_start_to_goal == float('inf')):

        print("\nNo optimal path found.")
    else:
        print("\nOptimal path found. Distance is " + str(distance_from_start_to_goal))
else:
    print("The entered goal node is an obstacle ")
