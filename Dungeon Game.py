class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self,dungeon):
        row,col=len(dungeon),len(dungeon[0])
        m=[[0 for y in range(col)] for x in range(row)]
        #init m[row-1][col-1]
        m[row-1][col-1]=(~dungeon[row-1][col-1])+2 if dungeon[row-1][col-1]<0 else 1
        #init m[row-1][j]
        for j in range(col-2,-1,-1):
            if dungeon[row-1][j] >= m[row-1][j+1]:
                m[row-1][j]=1
            else:
                m[row-1][j]=m[row-1][j+1]-dungeon[row-1][j]
        #init m[i][col-1]
        for i in range(row-2,-1,-1):
            if dungeon[i][col-1] >= m[i+1][col-1]:
                m[i][col-1]=1
            else:
                m[i][col-1]=m[i+1][col-1]-dungeon[i][col-1]
        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                select=min(m[i+1][j],m[i][j+1])
                if dungeon[i][j] >= select:
                    m[i][j]=1
                else:
                    m[i][j]=select-dungeon[i][j]
        return m[0][0]