"""8.8"""
class AStarMap:
	start = 0
	end = 0

	"""sortByFScore takes a list of nodes and sorts them by their own fscores. Required for AStar to work"""
	def sortByFScore(self,nodes): # heresy
		newSet = []
		for i in nodes:
			newSet+=[[i.FScore(),i]] # Make a list of lists whose first element is the fscore of each node and second element is the corresponding node
		newSet.sort() # sorteth the mall
		retSet = [] # this is the set we will be returning
		for i in newSet: 
			retSet+=[i[1]] # add all the nodes in order to this set
		return retSet # return that shiz
	
	"""CalculateGScore calculates the GScore Recursively from a given node back to the start. required for calculateFScore to work"""
	def calculateGScore(self,node):
		if(node == start): # the question is, Have you hit the star node yet?
			return node.cost # if youve recursed back far enough then youve hit the start node and can now return the whole cost.
		return node.cost + self.calculateGScore(node.parent) # returns the cost to go from the parent to the current node and recurses back
	
	"""Calculates the huristic score for the given node"""
	def calculateHScore(self,node):
		#These names are long and annoying and i dont want to deal with them.
		tx = self.target.position[0]
		ty = self.target.position[1]
		dx = node.position[0]
		dy = node.position[1]
		# Actual calculations of pythag
		cx = (tx - dx) ** 2
		cy = (ty - dy) ** 2
		c = (cx + cy) ** (1.0 / 2.0)
		return c

	"""calculates the FScore from the current point."""
	def calculateFScore(self,node):
		return self.calculateHScore(node) + self.calculateGScore(node) # Dat Sum Doh

	"""requires calculateFScore(), sortByFScore() to work!"""
	"""Takes two parameters start, for the start node, and end, for the target node. It then runs a* across the nodes."""
	def AStar(self, start, end):
		white = [] # List of nodes you havn't visited yet
		grey = [start] # List of TO EXPLORE nodes
		black = [] # List of been there done that nodes.

		while(len(grey)): # While grey list has literally anything at all
			grey = self.sortByFScore(grey) # Make sure they are in proper order
			
			for i in grey[0].getRogers(): # For each dude around the grey node
				if(grey.contains(i)):# if grey
					if(i.FScore() < self.calculateFScore(i)): # if its current fscore beats the currently proposed fscore
						continue # Skip it.
					else: # otherwise
						i.setFScore(self.calculateFScore(i)) # set it's new FScore
						i.setParent(grey[0]) # and it's new parent
			
			
				elif(black.contains(i)): #now if it is in the black node set (Same things really...)
					if(i.FScore() < self.calculateFScore(i)): # if its current fscore beats the currently propsed fscore
						continue # Skip it.
					else: # otherwise
						i.setFScore(self.calculateFScore(i)) # set the new Fscore
						i.setParent(grey[0]) # and it's new parent (again)
						grey += [i] # Add it back to the grey nodes. (finally something different)
		
				else: # if its white
					i.setFScore(calculateFScore(i)) # Set its FScore
					grey += [i] # Just add it already!
					continue # Move on if you just added it to the grey node list!

			black += [grey[0]] # Add the current grey node to the blacklist
			del grey[0] # Remove current grey node from greylist