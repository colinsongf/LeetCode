class Solution:
    def maxProfit_once(self,start,end,prices):
        maxprofit=0
        if end-start==0:
            return maxprofit
        buying=prices[start]
        for i in range(start+1,end+1):
            if prices[i]-buying>maxprofit:
                maxprofit=prices[i]-buying
            if prices<buying:
                buying=prices
        return maxprofit
    def maxProfit_once_fromhead(self,prices):#get maxprofit of [0...i]
        maxprofit=0
        size=len(prices)
        maxprofits=[0 for x in range(size)]
        if size<=1:
            return maxprofits
        minvalue=prices[0]
        for i,price in enumerate(prices):
            maxprofit=max(maxprofit,price - minvalue)
            maxprofits[i]=maxprofit
            minvalue=min(minvalue,price)
        return maxprofits
    def maxProfit_once_beforeend(self,prices):#get maxprofit of [i...size-1]
        maxprofit=0
        size=len(prices)
        maxprofits=[0 for x in range(size)]
        if size<=1:
            return maxprofits
        maxvalue=prices[size-1]
        for i,price in enumerate(reversed(prices)):
            maxprofit=max(maxprofit,maxvalue - price)
            maxprofits[size-1-i]=maxprofit
            maxvalue=max(maxvalue,price)
        return maxprofits
    def maxProfit(self, prices):
        maxprofit=0
        size=len(prices)
        if size<=1:
            return maxprofit
        fromhead=self.maxProfit_once_fromhead(prices)
        beforeend=self.maxProfit_once_beforeend(prices)
        maxprofit=fromhead[size-1]
        for k in range(size-1):
            maxprofit=max(maxprofit,fromhead[k]+beforeend[k+1])
        return maxprofit
