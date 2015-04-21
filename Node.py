class Node:
	position = [0,0]
	rogers = [0, 0, 0, 0, 0, 0, 0, 0]
	fscore = 0
	parent = 0
	cost = 0

	"""Returns the FScore of itself"""
	def FScore(self):
		return fscore
	"""sets the current parent to the given parent"""
	def setParent(self,newParent):
		self.parent = newParent
	"""sets the current fscore to the given fscore"""
	def setFScore(self,newFScore):
		self.fscore = newFScore
	"""Its a beautiful day."""
	def getRogers(self):
		return self.rogers