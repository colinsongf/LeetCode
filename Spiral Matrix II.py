class Solution:
    def writeCir(self,matrix,start,row,col,numbers):
        if row==1:
            matrix[start][start]=numbers.pop(0)
        else:
            for i in range(start,start+col):
                matrix[start][i]=numbers.pop(0)
            for i in range(start+1,start+row):
                matrix[i][start+col-1]=numbers.pop(0)
            for i in range(start+col-2,start-1,-1):
                matrix[start+row-1][i]=numbers.pop(0)
            for i in range(start+row-2,start,-1):
                matrix[i][start]=numbers.pop(0)
    def generateMatrix(self,n):
        matrix=[[0 for y in range(n)] for x in range(n)]
        numbers=[x for x in range(1,n**2+1)]
        row=col=n
        start=0
        while row>0 and col>0:
            self.writeCir(matrix,start,row,col,numbers)
            start+=1
            row-=2
            col-=2
        return matrix

ins=Solution()
print ins.generateMatrix(3)