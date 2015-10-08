class Solution:
	def getneibors(self,i,j,row,col):
		neibors=[]
		if i!=0:
			neibors.append((i-1,j))
		if j!=0:
			neibors.append((i,j-1))
		if i+1<row:
			neibors.append((i+1,j))
		if j+1<col:
			neibors.append((i,j+1))
		return neibors
	def getstartnode(self,grid,row,col,visited):
		for i in range(row):
			for j in range(col):
				if grid[i][j]=='1' and not visited[i][j]:
					return (i,j)
		return (-1,-1)
	def bfs(self,startnode,grid,row,col,visited):
		queue=[startnode]
		while queue:
			top=queue.pop()
			visited[top[0]][top[1]]=1
			neibors=self.getneibors(top[0],top[1],row,col)
			for neibor in neibors:
				if not visited[neibor[0]][neibor[1]] and grid[neibor[0]][neibor[1]]=='1':
					queue.append(neibor)
	def numIslands(self, grid):
		if not grid:
			return 0
		counter=0
		row,col=len(grid),len(grid[0])
		visited=[[0 for y in range(col)] for x in range(row)]
		startnode=self.getstartnode(grid,row,col,visited)
		while startnode!=(-1,-1):
			self.bfs(startnode,grid,row,col,visited)
			startnode=self.getstartnode(grid,row,col,visited)
			counter+=1
		return counter