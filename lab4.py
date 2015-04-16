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
def CSpaceMap(mapMsg):

	array = mapToArray(mapMsg)

	for i in range(mapMsg.info.width):
		for j in range(mapMsg.info.height):
			if (array[i][j] == 100):
				for k in range(-1,2):
					print k
					for l in range(-1,2):
						if ((i+k > 0 and i+k < mapMsg.info.width) and (j+l > 0 and j+l <mapMsg.info.height)):
							array[i+k][j+l]= max(50,array[i+k][j+l])


	for i in range(mapMsg.info.width):
		for j in range(mapMsg.info.height):
			if (array[i][j] == 50):
				array[i][j] = 100

	newArray = []

	for i in range(mapMsg.info.width):
		newArray = newArray + array[i]

	#print newArray
	mapMsg.data = tuple(newArray)

	return mapMsg

#turn a map into an array
def mapToArray(mapMsg):

	data = list(mapMsg.data)
	width = mapMsg.info.width
	height = mapMsg.info.height


	array = [0]*width
	array = [array]*height

	i = 0
	while (i < height):

		#print i

		array[i] = data[i*width:(i+1)*width]

		i += 1

	#print (len(array)), len(array[0])

	return array

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

def coor2Odom(coord, navMap):
	relCoord[0] = coord[0]*0

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
	expandMapPub = rospy.Publisher('/exmap',OccupancyGrid,queue_size=1)

	rospy.sleep(1)

	res = worldMap.info.resolution

	testCells = GridCells()
	testCells.cell_width = res
	testCells.cell_height = res
	testCells.header.frame_id = 'map'

	points = [Point(),Point(),Point(),Point()]
	points[1].x = 1.0*res
	points[2].y = 1.0*res
	points[3].x = 1.0*res
	points[3].y = 1.0*res

	testCells.cells = points

	testGridPub.publish(testCells)

	#print mapToArray(worldMap)

	#print testCells

	embiggenedMap = CSpaceMap(worldMap)

	#print embiggenedMap

	#initialize things
	position = [0, 0]
	robotOdom = odomCallBack(Odometry())

	#convert robot odometry to a node position on the map
	position = Odom2Coord(robotOdom, worldMap)

	while (True):
		testGridPub.publish(testCells)
		expandMapPub.publish(embiggenedMap)
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