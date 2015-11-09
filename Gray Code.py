class Solution:
    def handleanswer(self,answerList):
        answer=[]
        for bin in answerList:
            ret=0
            for bit in bin:
                ret=(ret<<1)+bit
            answer.append(ret)
        return answer
    def grayCode(self, n):
        if n==0:
            return [0]
        answerSize=2**n
        answerList=[[0 for x in range(n)] for y in range(answerSize)]
        for bit in range(1,n+1):
            split=2**bit
            blocksize=answerSize/split
            for row in range(answerSize):
                if (row/blocksize)&0x3==0:
                    answerList[row][bit-1]=0
                elif (row/blocksize)&0x3==1:
                    answerList[row][bit-1]=1
                elif (row/blocksize)&0x3==2:
                    answerList[row][bit-1]=1
                else:
                    answerList[row][bit-1]=0
        return self.handleanswer(answerList)
