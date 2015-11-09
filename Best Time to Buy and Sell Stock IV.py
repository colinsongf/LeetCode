class Solution:
    def maxProfit_best(self,prices,size):
        maxprofit=0
        for i in range(size-1):
            if prices[i+1]-prices[i]>0:
                maxprofit+=prices[i+1]-prices[i]
        return maxprofit
    def maxProfit(self, kmax , prices):
        size=len(prices)
        maxprofit=0
        if size<=1:
            return maxprofit
        if size/2<=kmax:
            return self.maxProfit_best(prices,size)
        m=[[0 for y in range(kmax+1)] for x in range(size)]
        for i in range(1,size):
            for k in range(1,kmax+1):
                m[i][k]=max(m[i-1][k],m[i][k-1])
                for j in range(1,i):
                    m[i][k]=max(m[i][k], m[j-1][k-1]+prices[i]-prices[j])
        return m[size-1][kmax]
