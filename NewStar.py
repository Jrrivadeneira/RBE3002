

class NewStar:
	worldMap=[]
	currentPosition=[]
	targetPosition=[]
	def __init__(self, myMap, currentPos, target):
		self.worldMap = myMap
		self.currentPosition=currentPos
		self.targetPosition=target

	def getPath(self):
		print "should be getting the path instaid of printing this line"
