class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
	def dfs_connect(self,coursemap,visited,startnode):
		if not coursemap[startnode]:
			visited[startnode]=2
			return True
		for neibor in coursemap[startnode]:
			if visited[neibor]==1:
				return False
			elif not visited[neibor]:
				visited[neibor]=1
				if not self.dfs_connect(coursemap,visited,neibor):
					return False
		visited[startnode]=2
		return True
	def dfs(self,coursemap,visited):
		for startnode in coursemap:
			if not visited[startnode]:
				visited[startnode]=1
				if not self.dfs_connect(coursemap,visited,startnode):
					return False
		return True
	def canFinish(self, numCourses, prerequisites):
		if not prerequisites:
			return True
		coursemap={}.fromkeys(range(numCourses),None)
		visited=[0 for i in range(numCourses)]
		for pairs in prerequisites:
			maincourse,prevcourse=pairs[0],pairs[1]
			if coursemap[prevcourse]:
				coursemap[prevcourse].append(maincourse)
			else:
				coursemap[prevcourse]=[maincourse]
		#dfs:
		return self.dfs(coursemap,visited)