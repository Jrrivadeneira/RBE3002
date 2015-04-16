 
class Node:
	# surrounding nodes
	rogers = [0, 0, 0, 0, 0, 0, 0, 0]
	# position
	position = []
	# Current G Score
	TheMagnificentG = 0
	# From
	origin = -1
	def __init__(self,pos,rogerz):
		self.rogers=self.rogerz
		self.position = pos
	# Problem Solved
	def getGScore(self, currentG):
		self.TheMagnificentG = currentG + ((10 + 4*(origin%2)) * (origin >= 0))
		return self.TheMagnificentG
	#
	def getHScore(self, target):
		x = self.position[0]
		y = self.position[1]
		tx = target[0]
		ty = target[1]
		return (((x - tx) ** 2) + ((y - ty) ** 2))) ** (0.5)

	def getFScore(self, GScore, target):
		return self.getHScore(target) + self.getGScore(GScore)

	def search(self,target, TheG, Open, Closed):
		if (self.position == target):
			return TheG
		# Get all the fscores for each surrounding node
		Fscorez = [[][]]
		for i in self.rogers:
			if(i==0):
				continue
			Fscorez[0] += [i.getFScore(TheG)]
			Fscorez[1] += [i]
		# Gets the next node in the path?
		# Figure out if you can put each one into the open set.
		for i in Fscorez:
			score = i[0]
			node = i[1]
		#	Is it in the closed set?
			if(node in Closed[1]):
				loca = Closed[1].index(node)
		#		is the Fscore better than the one in the closed set?
				if(score < Closed[0][loca]):
		#			remove it from the closed set
					del Closed[0][loca]
					del Closed[1][loca]			
				else:
					continue
		#	Is it in the open set?
			if(node in Open[1]):
				loca = Open[1].index(node)
		#		Is it's Fscore better than the one in the open set?
				if(Open[0][loca] > score): 
		#		replace the score and update the origin
					Open[0][loca] = score
					Open[1][loca].origin = Open[1][loca].rogers.index(node)
			else:
		#		add it outright otherwise
				Open[0] += [score]
				node.origin = node.rogers.index(self)
				Open[1] += [node]
		Closed[0] += self.getFScore(TheG)
		Closed[1] += self
		return [Open,Closed]

	def traceBack(self):
		if (self.origin == -1):
			return [self.location]
		return [self.rogers[self.origin].traceback] + [self.location]

	def findPath(self, finish):
		sets = self.search(finish, 0, [],[])
		Open = 0
		OpenSet = sets[Open]
		Closed = 1
		while(sets[Open] != []):
			sets = self.search(finish, 0, sets[Open], sets[Closed])
			sets[Open][0].index(set[Open][0].min())
