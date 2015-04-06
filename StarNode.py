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
	
	"""Constructor """
	def __init__(self, location, HScore, edges):
		self.location=location
		self.HScore = HScore
		self.edges = edges
		
	def calculateScores(self):
		calculateFScore()
		calculateGScore()
		calculateHScore()
		return 0

	"""get absolute distance from here to the end (pythagrian theroem"""
	def calculateHScore(self):
		return 0

	"""GScore of node that lead here plus distance of the edge between edge"""
	def calculateGScore(self):
		return 0

	"""sum of the GScore and the FScore"""
	def calculateFScore(self):
		return self.calculateGScore() + self.calculateHScore()
