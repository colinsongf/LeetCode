class Solution(object):
    def factorial(self, n):
        if n<=1:
            return 1
        else:
            return n*self.factorial(n-1)
    def uniquePaths(self, m, n):
        fenzi = self.factorial(m+n-2)
        fenmu = self.factorial(m-1)*self.factorial(n-1)
        return fenzi/fenmu