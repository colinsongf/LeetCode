class Solution(object):
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        d=[[0 for y in range(n)] for x in range(m)]
        d[0][0]=grid[0][0]
        for i in range(1,m):
            d[i][0]=d[i-1][0]+grid[i][0]
        for j in range(1,n):
            d[0][j]=d[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j]=min(d[i][j-1],d[i-1][j])+grid[i][j]
        return d[m-1][n-1]

ins=Solution()
print ins.minPathSum([[]])