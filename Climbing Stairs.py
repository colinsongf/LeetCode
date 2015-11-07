class Solution:
    def getSummary(self,answer,step):
        summary=0
        for ans in answer[:step]:
            summary+=ans
        return summary
    def availabe(self,answer,step,sel,n):
        summary=self.getSummary(answer,step)
        return summary+sel<=n
    def climbStairs(self,n):
        candidates=[1,2]
        answer,record=[0 for x in range(n)],[0 for x in range(n)]
        step,counter=0,0
        record[step]=-1
        while step>=0:
            record[step]+=1
            subSummary=self.getSummary(answer,step)
            if subSummary>n:
                step-=1
                continue
            while record[step]<2 and subSummary+candidates[record[step]]>n:
                record[step]+=1
            if record[step]==2:
                step-=1
            elif subSummary+candidates[record[step]]==n:
                answer[step]=candidates[record[step]]
                #print answer[:step+1]
                counter += 1
            else:
                answer[step]=candidates[record[step]]
                step+=1
                record[step]=-1
        return counter

ins = Solution()
print ins.climbStairs(35)