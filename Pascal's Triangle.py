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
    def generate(self,n):
        n-=1
        retlist=[]
        for i in range(n+1):
            ilist=[]
            for r in range(i+1):
                ilist.append(self.factorial(i,r))
            retlist.append(ilist)
        return retlist