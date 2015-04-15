import numpy

class StarNode:
	"""docstring for StarNode"""
	location = []
	currentState = 0
	edges = []
	FScore = 0.0
	GScore = 0.0
	HScore = 0.0
	FromNodes = []
	ToNodes = []
	parent = None
	"""Constructor """
	def __init__(self, location, parent):
		self.location = location
		self.parent = parent

	""" Returns a list representation of this node"""
	def toList(self):
		return [self.FScore,self.location,self.currentState,self.edges,self.GScore,self.HScore,self.FromNodes,self.ToNodes]
	
	"""sets this node according to hte given list"""
	def setList(self, lis):
		self.FScore = lis[0]
		self.location = lis[1]
		self.currentState = lis[2]
		self.edges = lis[3]
		self.GScore = lis[4]
		self.HScore = lis[5]
		self.FromNodes = lis[6]
		self.ToNodes = lis[7]

	def calculateScores(self, dest):
		self.calculateFScore(dest)

		return 0

	"""get absolute distance from here to the end (pythagrian theroem)"""
	def calculateHScore(self, dest):
		self.HScore = numpy.sqrt((dest[0]-self.location[0])**2 + (dest[1]-self.location[1])**2)
		#print "HScore = ", self.HScore
		return self.HScore

	"""GScore of node that lead here plus distance of the edge between edge"""
	def calculateGScore(self):
		if len(self.FromNodes) > 0:
			self.GScore = self.FromNodes[0].GScore + numpy.sqrt((self.FromNodes[0].location[0]-self.location[0])**2 + (self.FromNodes[0].location[1]-self.location[1])**2)
		self.GScore = 99999
		#print "GScore = ", self.GScore	
		return self.GScore

	"""sum of the GScore and the FScore"""
	def calculateFScore(self, dest):

		self.calculateGScore()
		self.calculateHScore(dest)

		self.FScore = self.GScore + self.HScore
		#print "FScore = ", self.FScore	
		return self.FScore
