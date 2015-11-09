class Solution:
    def printCir(self,matrix,start,row,col):
        subanswer=[]
        if row==1:
            for i in range(start,start+col):
                subanswer.append(matrix[start][i])
        elif col==1:
            for i in range(start,start+row):
                subanswer.append(matrix[i][start])
        else:
            for i in range(start,start+col):
                subanswer.append(matrix[start][i])
            subanswer.pop()
            for i in range(start,start+row):
                subanswer.append(matrix[i][start+col-1])
            subanswer.pop()
            for i in range(start+col-1,start-1,-1):
                subanswer.append(matrix[start+row-1][i])
            subanswer.pop()
            for i in range(start+row-1,start-1,-1):
                subanswer.append(matrix[i][start])
            subanswer.pop()
        return subanswer
    def spiralOrder(self,matrix):
        answer=[]
        row=len(matrix)
        if not row:
            return answer
        col=len(matrix[0])
        start=0
        while row>0 and col>0:
            subans=self.printCir(matrix,start,row,col)
            row-=2
            col-=2
            start+=1
            answer.extend(subans)
        return answer
