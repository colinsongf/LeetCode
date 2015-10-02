class Solution:
	def maxProfit(self, prices):
		maxprofit,size = 0,len(prices)
		if size<2:
			return maxprofit
		minvalue = prices[0]
		for i in range(1,size):
			if maxprofit < prices[i]-minvalue:
				maxprofit = prices[i]-minvalue
			if minvalue > prices[i]:
				minvalue = prices[i]
		return maxprofit

ins=Solution()
print ins.maxProfit([])