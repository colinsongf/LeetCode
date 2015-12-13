class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def twoSum(self,num,answer,target,start,end,item1,item2):
        i,j=start,end
        flag=False
        while i<j:
            if num[i]+num[j]==target:
                previ,prevj=num[i],num[j]
                while i<=end and num[i]==previ:
                    i+=1
                while j>=0 and num[j]==prevj:
                    j-=1
                thisanswer=[item1,item2,previ,prevj]
                answer.append(thisanswer)
                flag=True
            elif num[i]+num[j]>target:
                j-=1
            else:
                i+=1
        return flag
    def fourSum(self, num, target):
        answer=[]
        size=len(num)
        num.sort()
        prev=None
        if size<4:
            return answer
        ever=[]
        for i in range(size-3):
            for j in range(i+1,size-2):
                if (num[i],num[j]) in ever:
                    continue
                subtarget=target-(num[i]+num[j])
                if self.twoSum(num,answer,subtarget,j+1,size-1,num[i],num[j]):
                    ever.append((num[i],num[j]))
                prev=num[j]
        return answer