class StarNode:
	"""docstring for StarNode"""
	location = []
	currentState = 0
	edges = []
	FFScore = 0.0
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
		return [self.FFScore,self.location,self.currentState,self.edges,self.GScore,self.HScore,self.FromNodes,self.ToNodes]
	
	"""sets this node according to hte given list"""
	def setList(self, lis):
		self.FFScore = lis[0]
		self.location = lis[1]
		self.currentState = lis[2]
		self.edges = lis[3]
		self.GScore = lis[4]
		self.HScore = lis[5]
		self.FromNodes = lis[6]
		self.ToNodes = lis[7]

	def calculateScores(self):
		self.calculateFFScore()
		self.calculateGScore()
		self.calculateHScore()
		return 0

	"""get absolute distance from here to the end (pythagrian theroem)"""
	def calculateHScore(self):
		return 0

	"""GScore of node that lead here plus distance of the edge between edge"""
	def calculateGScore(self):
		return 0

	"""sum of the GScore and the FFScore"""
	def calculateFScore(self):
		return self.calculateGScore() + self.calculateHScore()
