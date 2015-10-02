class Solution:
	def __init__(self):
		self.board=[[0 for y in range(9)] for x in range(9)]
	def avaliable(self,x,y,sel,board):
		for j in range(9):
			if board[x][j]==sel:
				return False
		for i in range(9):
			if board[i][y]==sel:
				return False
		rowStart,rowEnd=-1,-1
		if 0<=x<=2:
			rowStart,rowEnd=0,2
		elif 3<=x<=5:
			rowStart,rowEnd=3,5
		else:
			rowStart,rowEnd=6,8
		colStart,colEnd=-1,-1
		if 0<=y<=2:
			colStart,colEnd=0,2
		elif 3<=y<=5:
			colStart,colEnd=3,5
		else:
			colStart,colEnd=6,8
		for i in range(rowStart,rowEnd+1):
			for j in range(colStart,colEnd+1):
				if board[i][j]==sel:
					return False
		return True
	def getInitCandidates(self,x,y,board):
		rowHash={}.fromkeys([str(i) for i in range(1,10)],0)
		colHash={}.fromkeys([str(i) for i in range(1,10)],0)
		cubeHash={}.fromkeys([str(i) for i in range(1,10)],0)
		for j in range(9):
			if board[x][j]!='.':
				rowHash[board[x][j]]=1
		for i in range(9):
			if board[i][y]!='.':
				colHash[board[i][y]]=1
		rowStart,rowEnd=-1,-1
		if 0<=x<=2:
			rowStart,rowEnd=0,2
		elif 3<=x<=5:
			rowStart,rowEnd=3,5
		else:
			rowStart,rowEnd=6,8
		colStart,colEnd=-1,-1
		if 0<=y<=2:
			colStart,colEnd=0,2
		elif 3<=y<=5:
			colStart,colEnd=3,5
		else:
			colStart,colEnd=6,8
		for i in range(rowStart,rowEnd+1):
			for j in range(colStart,colEnd+1):
				if board[i][j]!='.':
					cubeHash[board[i][j]]=1
		candidates1=set([x for x in rowHash if rowHash[x]==0])
		candidates2=set([x for x in colHash if colHash[x]==0])
		candidates3=set([x for x in cubeHash if cubeHash[x]==0])
		return candidates1&candidates2&candidates3
	def recordAns(self,board):
		for i in range(9):
			for j in range(9):
				self.board[i][j]=board[i][j]
	def writeBoard(self,board):
		for i in range(9):
			for j in range(9):
				board[i][j]=self.board[i][j]
	def backtrace(self,step,handle,board,size):
		if step==size:
			self.recordAns(board)
			return
		x,y,candidates=handle[step]
		for candidate in candidates:
			if not self.avaliable(x,y,candidate,board):
				continue
			old=board[x][y]
			board[x][y]=candidate
			self.backtrace(step+1,handle,board,size)
			board[x][y]=old
	def solveSudoku(self, board):
		handle=[]
		for i in range(9):
			for j in range(9):
				if board[i][j]=='.':
					handle.append((i,j,self.getInitCandidates(i,j,board)))
		handle.sort(key=lambda x:len(x[2]))
		self.backtrace(0,handle,board,len(handle))
		self.writeBoard(board)

board=[['.','.','9','7','4','8','.','.','.'],
['7','.','.','.','.','.','.','.','.'],
['.','2','.','1','.','9','.','.','.'],
['.','.','7','.','.','.','2','4','.'],
['.','6','4','.','1','.','5','9','.'],
['.','9','8','.','.','.','3','.','.'],
['.','.','.','8','.','3','.','2','.'],
['.','.','.','.','.','.','.','.','6'],
['.','.','.','2','7','5','9','.','.']]
ins=Solution()
ins.solveSudoku(board)