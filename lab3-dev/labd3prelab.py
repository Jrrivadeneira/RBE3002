import rospy, roslib
from nav_msgs.msg import *
from nav_msgs.srv import *
from StarMap import *
"""Documentation"""
def mapCallback(msg):
	global current_map

	print msg

	#setting the global map
	current_map = msg



def odomCallback(msg):
	global starting_pos
	global current_map

	starting_pos = msg.pose.pose.position
	starting_odom = msg.pose.pose.Odometry


def printInfo(msg):
	print 'starting_pos'
	print 'starting_odom'
	print 'current_map'

#using some stuff from this:
#https://github.com/Peaches491/DM_3002/blob/master/dm_a_star/src/astar.py
def mapMap():
	request = GetMapRequest()
	rospy.sleep(rospy.Duration(1,0))
	return request

def GetMapRequest():
	return


if __name__ == '__main__':
	rospy.init_node('nodesdontnodenodes_nodesnodesnodes')

	global mapSub
	global odomSub
	global current_map

	current_map = 0

	#subscribe to the map
	mapSub = rospy.Subscriber('/map',OccupancyGrid, mapCallback, queue_size=1)
	odomSub = rospy.Subscriber('/odom', Odometry, odomCallback, queue_size=1)

	mapMap()
	
	mapPub1 = rospy.Publisher('/map1', OccupancyGrid, queue_size=1)

	print current_map

	CMList = list(current_map.data)

	current_map.data = tuple(CMList)

	newMap = OccupancyGrid()
	newMap.header.frame_id = 'map1'
	newMap.header.stamp = rospy.Time.now()
	newMap.info = current_map.info
	newMap.info.map_load_time = rospy.Time.now()
	newMap.data = current_map.data

	print "test"

	mapPub1.publish(newMap)

	navmap = StarMap(37, 37, CMList,[2,2],[5, 2])

	navmap.showMap()
	navmap.createMap()

	exit()
	
