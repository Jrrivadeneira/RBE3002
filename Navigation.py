""" 
Navi Class
purpose of this class is to allow for navigation down a path.
	calculate paths
	get next node in path
	go there
	repeat
"""

class Navi:
	worldMap = []
	currentPosition = []
	targetPosition = []
	
	def setMap(self, newMap):
		self.worldMap = newMap

	def setPosition(self, newPosition):
		self.currentPosition = newPosition
	
	def setTarget(self,newTarget):
		self.targetPosition = newTarget

	def navigate(self):
		target = self.targetPosition
		position = self.currentPosition
		world = self.worldMap
		
