class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		m,n=len(obstacleGrid),len(obstacleGrid[0])
		d=[[0 for x in range(n)] for y in range(m)]
		#init
		d[0][0] = 0 if obstacleGrid[0][0] else 1
		for j in range(1,n):
			d[0][j]=d[0][j-1] if not obstacleGrid[0][j] else 0
		for i in range(1,m):
			d[i][0]=d[i-1][0] if not obstacleGrid[i][0] else 0
		#dynamic
		for i in range(1,m):
			for j in range(1,n):
				d[i][j]=0
				if not obstacleGrid[i-1][j]:
					d[i][j] += d[i-1][j]
				if not obstacleGrid[i][j-1]:
					d[i][j] += d[i][j-1]
				if obstacleGrid[i][j]:
					d[i][j]=0
		return d[m-1][n-1]

ins = Solution()
print ins.uniquePathsWithObstacles([[0,0],[0,1]])