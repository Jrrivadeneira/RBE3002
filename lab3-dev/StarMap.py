"""
StarMap
Written by Jack Rivadeneira
"""

import rospy

from StarNode import StarNode
class StarMap:
	"""Object variables"""
	x = 3
	y = 4
	givenMap = []
	start = [0,0]
	finish = [0,0]
	closedSet = []
	openSet = []
	path = []

	"""Constructor """
	def __init__(self, x, y, givenMap, start, finish):
		self.x = x
		self.y = y
		self.start = start
		self.finish = finish
		i = 0
		while(i < y):
			self.givenMap += [givenMap[:x]]
			givenMap = givenMap[x:]
			i += 1

	"""return the set of cells which is the most efficient path"""
	def rebuildPath(self, node):
		path = [node]

		while node.location != self.start:
			print node.location, node
			node = node.FromNodes[0]

		return path

		if node == None:
			return path
		path += self.rebuildPath(node.FromNodes[0])
		return

	"""Shows the map it is currently dealing with"""
	def showMap(self):
		i = 0
		while(i < len(self.givenMap)):
			i+=1
		return i

	"""returns the node with the smallest F score"""
	def minF(self, openSet):
		pivot = 999999999
		smallest = openSet[0]
		for i in openSet:
			if i.FScore < pivot:
				smallest = i
				pivot = i.FScore

		return smallest

	"""gets the current width of the map (number of columns"""
	def getWidth(self):
		return self.x

	"""gets the current height of the map (number of rows)"""
	def getHeight(self):
		return self.y

	"""Checks if a given point is valid."""
	def isValidPoint(self, point):
		return ((point[0] < self.getWidth() and point[0] >= 0) and (point[1] < self.getHeight() and point[1] >= 0))

	""" Checks to see if the given points contain the same values. """
	def isSamePoint(self,A,B):
		return ((A[0] == B[0]) and (A[1] == B[1]))

	""" Checks to see if the given point is vacant. """
	def isVacantPoint(self,point):
		return self.givenMap[point[0]][point[1]] == 0

	""" Returns a list of points that you can go to from the given point. """
	def getOptions(self,point):
		# get directions to evaluate 
		up = [point[0], point[1] - 1]
		down = [point[0], point[1] + 1]
		left = [point[0] - 1, point[1]]
		rite = [point[0] + 1, point[1]]
		topLeft = [point[0] - 1, point[1] - 1]
		topRite = [point[0] + 1, point[1] - 1]
		botLeft = [point[0] - 1, point[1] + 1]
		botRite = [point[0] + 1, point[1] + 1]
		# add them to the directions list (for the sake of extensibility)
		directions = [up,down,left,rite,topRite,topLeft,botRite,botLeft]
		# check if points are valid or occupied and if they are eliminate them.
		fakeInternetPoints = []
		for pt in directions:
			# if(self.isValidPoint(pt) and self.isVacantPoint(pt)):
			if(self.isValidPoint(pt)):
				fakeInternetPoints += [self.givenMap[pt[0]][pt[1]]]
		# return the valid points. 
		return fakeInternetPoints

	"""TODO: IMPLEMNT THIS FUNCTION! Returns the distance between the two given points"""
	def distanceTo(self,currentPoint,targetPoint):
		return 0

	"""Returns the point that is closer to the target"""
	def closestPoint(self,pointA,pointB,target):
		if(self.distanceTo(pointA,target)>self.distanceTo(pointB,target)):
			return pointB
		return pointA

	"""I need a thing to find the best route from one point to another.
	Do diagonals count?"""
	def createMap(self):
		yp = 0
		while(yp < self.getHeight()):
			xp = 0
			while(xp < self.getWidth()):
				if(self.isVacantPoint([xp,yp])):
					self.givenMap[xp][yp] = StarNode([xp,yp], self)
				xp += 1
			yp += 1
		yp = 0
		while(yp < self.getHeight()):
			xp = 0
			while(xp < self.getWidth()):
				# add edges by using the get options
				if self.givenMap[xp][yp] != 100:
					self.givenMap[xp][yp].edges = self.getOptions([xp,yp])
				xp += 1
			yp += 1
		#linearizin the list
		linearList = []
		for i in self.givenMap:
			linearList+=i
		sortedList = []
		for i in linearList:
			if i != 100:
				i.calculateScores(self.finish)
				sortedList += [i.toList()]
		sortedList.sort()
		sortedList.reverse()
		
		for i in linearList:
			if i != 100:
				i.calculateScores(self.finish)
				
				#this code is based off of the pseudocode on Wikipedia about A*
				closedSet = []
				openSet = []

				#find the start node
				if i.location == self.start:

					#set the from node of each edge to the start node
					for j in i.edges:
						j.FromNodes = [i]
						j.calculateScores(self.finish)
					print "found start at ", i.location
					i.GScore = 0

					openSet = i.edges
					closedSet = [i]

					while len(openSet) > 0:
						current = self.minF(openSet) #lowest FScore

						if current.location == self.finish:
							return self.rebuildPath(current)

						closedSet.append(current)
						openSet.remove(current)
						for fblthp in current.edges:

							if fblthp == 100:
								break

							tentativeG = 0
							if fblthp in closedSet:
								tentativeG = current.GScore #distance between current and fblthp

							if (not fblthp in openSet) or (tentativeG <= fblthp.GScore):
								fblthp.FromNodes.append(current)
								fblthp.calculateScores(self.finish)
								if fblthp not in openSet:
									openSet.append(fblthp)

					return false


# print k.showMap()
# print k.givenMap[0][0].edges
