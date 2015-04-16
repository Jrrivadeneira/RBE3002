import rospy, tf
import StarMap
from nav_msgs.srv import GetMapRequest, GetMapResponse
from nav_msgs.msg import Odometry
from nav_msgs.msg import OccupancyGrid, GridCells
from geometry_msgs.msg import PoseStamped, Point

worldMap = 0

"""callbacks"""
def mapCallBack(msg):
	#while (msg == OccupancyGrid()):
		#rospy.sleep(0.01)
	global worldMap
	worldMap = msg
	return msg

def odomCallBack(msg):
	return msg

def goalCallBack(msg):
	return msg

#subscribe to waypoints from rviz
def InitSubs():
	mapSub = rospy.Subscriber(rospy.get_param('/map_input_topic','/map'),OccupancyGrid, mapCallBack, queue_size=1)
	odomSub = rospy.Subscriber('/odom', Odometry, odomCallBack, queue_size=1)
	goalSub = rospy.Subscriber('/move_base_simple/goal', PoseStamped, goalCallBack, queue_size=1)

	return [mapSub, odomSub, goalSub]

#publish map
def CSpaceMap():

	return

"""convert an Odometry object to a coordinate on the map"""
def Odom2Coord(odom, navMap):
	
	#this is the robot in the global coordinate system
	relCoord = [odom.pose.pose.position.x,odom.pose.pose.position.y] 

	#this is the position of the robot relative to the center of the map in meters
	relCoord[0] -= navMap.info.origin.position.x
	relCoord[1] -= navMap.info.origin.position.y

	#convert units to gridcells
	relCoord[0] /= navMap.info.resolution
	relCoord[1] /= navMap.info.resolution

	#round to be an actual cell
	relCoord = [round(relCoord[0],0),round(relCoord[1],0)]

	return relCoord

"""navigate to a point"""
def Nav2Point(start, goal, worldMap):

	#code goes here

	return

"""main function"""
if __name__ == '__main__':
	rospy.init_node('nodesdontnodenodes_nodesnodesnodes')

	#subscribe to relevant topics with SubsNPubs function
	[mapSub, odomSub, goalSub] = InitSubs()

	testGridPub = rospy.Publisher('/testGrid', GridCells, queue_size=1)

	rospy.sleep(1)

	testCells = GridCells()
	testCells.cell_width = worldMap.info.resolution
	testCells.cell_height = testCells.cell_width
	testCells.header.frame_id = 'map'

	points = [Point(),Point(),Point(),Point()]
	points[1].x = 1.0
	points[2].y = 1.0
	points[3].x = 1.0
	points[3].y = 1.0

	testCells.cells = points

	testGridPub.publish(testCells)

	print testCells

	#initialize things
	position = [0, 0]
	robotOdom = odomCallBack(Odometry())

	#convert robot odometry to a node position on the map
	position = Odom2Coord(robotOdom, worldMap)

	while (True):
		testGridPub.publish(testCells)
		rospy.sleep(1)

	#always be navigating
	while (True):

		#if the robot has not reached the goal
		if (position != target):

			#run A* to return the location of the next node to navigate to
			target = navigateTo(position,goal)

			#turn to face it

			#move forward until in target cell

			#convert robot odometry to a node position on the map
			position = Odom2Coord(robotOdom, worldMap)
		else:
			rospy.sleep(rospy.Duration(1,0))