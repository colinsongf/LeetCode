class Solution:
    def available(self,answer,step,sel):
        ok=True
        for i in range(step):
            if answer[i]==sel or abs(step-i)==abs(sel-answer[i]):
                ok=False
                break
        return ok
    def getanswer(self,answer,n):
        answerlist=[]
        for i in answer:
            substr='.'*i+'Q'+'.'*(n-1-i)
            answerlist.append(substr)
        return answerlist
    def solveNQueens(self ,n):
        answerset=[]
        answer,record=[0 for x in range(n)],[0 for x in range(n)]
        step=0
        record[step]=-1
        while step>=0:
            record[step]+=1
            while record[step]<n and not self.available(answer,step,record[step]):
                record[step]+=1
            if record[step]==n:
                step-=1
            elif step==n-1:
                answer[step]=record[step]
                answerset.append(self.getanswer(answer,n))
            else:
                answer[step]=record[step]
                step+=1
                record[step]=-1
        return answerset