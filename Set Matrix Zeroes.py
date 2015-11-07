class Solution(object):
    def setZeroes(self, matrix):
        row_record,col_record=0,0
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(col):
                if not matrix[i][j]:
                    row_record |= (1<<i)
                    col_record |= (1<<j)
        for i in range(row):
            if row_record & (1<<i):
                for j in range(col):
                    matrix[i][j]=0
        for j in range(col):
            if col_record & (1<<j):
                for i in range(row):
                    matrix[i][j]=0

ins=Solution()
matrix = [[1,2,3],
            [4,0,6],
            [7,8,0]]
ins.setZeroes(matrix)

print matrix