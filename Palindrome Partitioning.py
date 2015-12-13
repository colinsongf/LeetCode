class Solution:
    def __init__(self):
        self.answerList=[]
    def isPali(self,string,i,j):
        while i<=j:
            if string[i]==string[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    def handleAnswer(self,answer,string,size):
        answerlist=[]
        prev=0
        for pos in answer:
            answerlist.append(string[prev:pos+1])
            prev=pos+1
        return answerlist
    def backtrace(self,palidict,string,size,answer,startpos):
        if startpos==size:
            someanswer=self.handleAnswer(answer,string,size)
            self.answerList.append(someanswer)
            return
        for endnode in palidict[startpos]:
            answer.append(endnode)
            startpos=endnode+1
            self.backtrace(palidict,string,size,answer,startpos)
            answer.pop()
    def partition(self, string):
        size=len(string)
        palidict={}
        for i in range(size):
            palidict[i]=[]
            for j in range(i,size):
                if self.isPali(string,i,j):
                    palidict[i].append(j)
        answer=[]
        self.backtrace(palidict,string,size,answer,0)
        return self.answerList
