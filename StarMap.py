import numpy

class StarMap:
	"""Object variables"""
	x = 3
	y = 4
	givenMap = []

	"""Constructor """
	def __init__(self, x, y, givenMap):
		self.x = x
		self.y = y
		i = 0
		print "start"
		while(i < y):
			self.givenMap += [givenMap[:x]]
			givenMap = givenMap[x:]
			i += 1

	"""Shows the map it is currently dealing with"""
	def showMap(self):
		i = 0
		while(i < len(self.givenMap)):
			print self.givenMap[i]
			i+=1
		return i

	"""gets the current width of the map (number of columns"""
	def getWidth(self):
		return self.x

	"""gets the current height of the map (number of rows)"""
	def getHeight(self):
		return self.y

	"""Checks if a given point is valid."""
	def isValidPoint(self, point):
		return ((point[0] < self.getWidth() and point[0] > 0) and (point[1] < self.getHeight() and point[1] > 0))

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
		# add them to the directions list (for the sake of extensibility)
		directions = [up,down,left,rite]
		# check if points are valid or occupied and if they are eliminate them.
		fakeInternetPoints = []
		for pt in directions:
			if(self.isValidPoint(pt) and self.isVacantPoint(pt)):
				fakeInternetPoints += [pt]
		return fakeInternetPoints

	"""TODO: IMPLEMNT THIS FUNCTION! Returns the distance between the two given points"""
	def distanceTo(self,currentPoint,targetPoint):
		return numpy.sqrt((currentPoint[0] - targetPoint[0])^2 + (currentPoint[1] - targetPoint[1])^2)

	"""Returns the point that is closer to the target"""
	def closestPoint(self,pointA,pointB,target):
		if(self.distanceTo(pointA,target)>self.distanceTo(pointB,target)):
			return pointB
		return pointA


	"""I need a thing to find the best route from one point to another.
	Do diagonals count?"""
	def getPath(self, currentPosition, targetPosition, currentPath):
		# Validate points
		if(not (self.isValidPoint(currentPosition) and self.isValidPoint(targetPosition))):
			print "Bad Points!"
			return []
		# Are we there yet?
		if(self.isSamePoint(currentPosition,targetPosition)):
			print currentPath
			return currentPath
		# The hard part.
		# The points are valid and we aren't already there.
		# Damn it.
		# We need to get a list of locations we can go from our current position.
		locations = self.getOptions(currentPosition)
		# we need to decide which of these are closest to our goal.
		closest = locations[0]
		for i in locations[1:]:
			closest = self.closestPoint(closest,i,targetPosition)
		# we need to change our current position to that point.
		# continue doing this.
		# what if you hit a dead end?
		# Then you need to expand outward and find your way around the dead end.




"""k = StarMap(37,37,[0]*37*37)
print k.showMap()
print k.getPath([4,3],[32,24],[])"""
