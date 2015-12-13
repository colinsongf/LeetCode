class Solution:
    def available(self,answer,step,sel,n):
        pos,neg=0,0
        for i in range(step):
            if answer[i]:
                pos+=1
            else:
                neg+=1
        if sel:
            pos+=1
        else:
            neg+=1
        return (pos>=neg) and (pos<=n)
    def makeans(self,answer):
        answerStr=''
        for sig in answer:
            if sig:
                answerStr+='('
            else:
                answerStr+=')'
        return answerStr
    def generateParenthesis(self,n):
        selections=[1,0]
        step=0
        answer,record=[0 for x in range(2*n)],[0 for x in range(2*n)]
        record[step]=-1
        answerList=[]
        while step>=0:
            record[step]+=1
            while record[step]<2 and not self.available(answer,step,selections[record[step]],n):
                record[step]+=1
            if record[step]==2:
                step-=1
            elif step==2*n-1:
                answer[step]=selections[record[step]]
                answerList.append(self.makeans(answer))
            else:
                answer[step]=selections[record[step]]
                step+=1
                record[step]=-1
        return answerList