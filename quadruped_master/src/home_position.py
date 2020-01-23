#!/usr/bin/env python
import numpy as np
import rospy
import math
import tf
import sys
import copy
import geometry_msgs.msg
import moveit_commander
import moveit_msgs.msg
import random
import cv2
import cv_bridge
import rospkg
import os


from moveit_commander import MoveGroupCommander


# Main portion of code
def main():


	# Initialize node
	rospy.init_node('Home_position')

    #Instantiate a RobotCommander object. This object is an interface to the robot as a whole.
	robot = moveit_commander.RobotCommander()

	#Wait for RVIZ to initialize. This sleep is ONLY to allow Rviz to come up.
	print "============ Waiting for RVIZ..."
	rospy.sleep(5)
	print "============ Starting tutorial "

	#Instantiate a PlanningSceneInterface object. This object is an interface to the world surrounding the robot.
	global scene
	scene = moveit_commander.PlanningSceneInterface()
	rospy.sleep(1)

	#Instantiate a MoveGroupCommander object. This object is an interface to one group of joints. In this case the group is the joints in the left arm. This interface can be used to plan and execute motions on the left arm.
	global group_robot, group_front_right_leg, group_front_left_leg
	group_robot = MoveGroupCommander("robot")
	group_robot.set_goal_position_tolerance(0.05)
	group_robot.set_goal_orientation_tolerance(0.05)
	group_robot.set_planning_time(5.0)
    
    # We create this DisplayTrajectory publisher which is used below to publish trajectories for RVIZ to visualize.
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

	#mption of the robot
	# home_joints_position = {'front_right_joint1': 0, 'front_left_joint1': 0, 'back_right_joint1': 0, 'back_left_joint1': 0, 'front_right_joint2': 0, 'front_left_joint2': 0, 'back_right_joint2': 0, 'back_left_joint2': 0}
	home_joints_position = {'front_right_joint1': 0.5, 'front_left_joint1': 0.5, 'back_right_joint1': 0.5, 'back_left_joint1': 0.5, 'front_right_joint2': 0.5, 'front_left_joint2': 0.5, 'back_right_joint2': 0.5, 'back_left_joint2': 0.5}
	group_robot.set_joint_value_target(home_joints_position)
	plan_both = group_robot.plan()
	group_robot.execute(plan_both)

if __name__ == '__main__':
	main()