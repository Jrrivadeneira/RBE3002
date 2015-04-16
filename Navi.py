""" 
Navi Class
purpose of this class is to allow for navigation down a path.
"""

class Navi:
	worldMap = []
	currentPosition = []
	targetPosition = []
	def navigateTo(self, target):
		self.targetPosition = target
