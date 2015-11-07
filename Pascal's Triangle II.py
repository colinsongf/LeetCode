class Solution:
    def factorial(self,n,r):
        mother,child,i = 1,1,0
        while i<=(r-1):
            mother*=(n-i)
            i+=1
        while r:
            child*=r
            r-=1
        return mother/child
    def getRow(self,n):
        ilist=[]
        for r in range(n+1):
            ilist.append(self.factorial(n,r))
        return ilist