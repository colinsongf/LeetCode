class Solution:
    def binarysearch(self,num,i,j,target):
        while i<=j:
            mid=i+j>>1
            if num[mid]==target:
                return mid
            elif num[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return -1
    def search(self,num,target):
        size=len(num)
        i,j=0,size-1
        if num[i]<=num[j]:
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
        if target<num[minPos] or target>num[minPos-1]:
            return -1
        if num[0]<=target:
            return self.binarysearch(num,0,minPos-1,target)
        else:
            return self.binarysearch(num,minPos,size-1,target)
