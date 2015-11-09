class Solution(object):
    def getPermutation(self,n,k):
        currentArr = range(1,n+1)
        currentK = 1
        while currentK < k:
            i,j = n-2,n-1
            while i>=0 and currentArr[i]>currentArr[j]:
                i-=1;j-=1
            if i==-1:
                break
            currentArr[j:]=reversed(currentArr[j:])
            for pos in range(j,n):
                if currentArr[pos] > currentArr[i]:
                    currentArr[i],currentArr[pos] = currentArr[pos],currentArr[i]
                    break
            currentK += 1
        return ''.join([str(x) for x in currentArr])
