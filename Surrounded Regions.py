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
	def solve(self,board):
		if not board:
			return
		row,col=len(board),len(board[0])
		visited=[[0 for y in range(col)] for x in range(row)]
		starts=[]
		for j in range(col):
			if board[0][j]=='O':
				starts.append((0,j))
			if board[row-1][j]=='O':
				starts.append((row-1,j))
		for i in range(row):
			if board[i][0]=='O':
				starts.append((i,0))
			if board[i][col-1]=='O':
				starts.append((i,col-1))
		for start in starts:
			x,y=start
			if visited[x][y]:
				continue
			queue=[start]
			while queue:
				top=queue.pop()
				i,j=top
				visited[i][j]=1
				neibors=self.getneibors(i,j,row,col)
				for neibor in neibors:
					if board[neibor[0]][neibor[1]]=='O' and visited[neibor[0]][neibor[1]]==0:
						queue.append(neibor)
		for i in range(row):
			for j in range(col):
				if board[i][j]=='O' and not visited[i][j]:
					board[i][j]='X'