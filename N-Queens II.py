class Solution:
    def available(self,answer,step,sel):
        ok=True
        for i in range(step):
            if answer[i]==sel or abs(step-i)==abs(sel-answer[i]):
                ok=False
                break
        return ok
    def totalNQueens(self ,n):
        answer,record=[0 for x in range(n)],[0 for x in range(n)]
        step=0
        counter=0
        record[step]=-1
        while step>=0:
            record[step]+=1
            while record[step]<n and not self.available(answer,step,record[step]):
                record[step]+=1
            if record[step]==n:
                step-=1
            elif step==n-1:
                answer[step]=record[step]
                counter+=1
            else:
                answer[step]=record[step]
                step+=1
                record[step]=-1
        return counter

ins=Solution()
print ins.totalNQueens(8)