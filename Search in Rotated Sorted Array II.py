class Solution:
    def getMinPos(self,num):
        minPos=len(num)-1
        while minPos>=1 and num[minPos-1]<=num[minPos]:
            minPos-=1
        return minPos
    def binarysearch(self,num,i,j,target):
        while i<=j:
            mid=i+j>>1
            if num[mid]==target:
                return True
            elif num[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return False
    def search(self,num,target):
        size=len(num)
        i,j=0,size-1
        if size==1:
            return num[0]==target
        if num[i]<num[j]:
            return self.binarysearch(num,i,j,target)
        minPos=-1
        while i<j:
            if i==j-1:
                minPos = j
                break
            mid=i+j>>1
            if num[mid]>num[i]:
                i=mid
            elif num[mid]<num[j]:
                j=mid
            else:
                minPos=self.getMinPos(num)
                break
        #print minPos
        if target<num[minPos] or target>num[minPos-1]:
            return False
        if num[0]<=target:
            return self.binarysearch(num,0,minPos-1,target)
        else:
            return self.binarysearch(num,minPos,size-1,target)
