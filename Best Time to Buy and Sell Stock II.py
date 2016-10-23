class Solution:
    # @param prices, a list of integer
    # @return an integer
	def maxProfit(self, prices):
		summary,size=0,len(prices)
		for i in range(size-1):
			if prices[i+1]-prices[i]>0:
				summary+=prices[i+1]-prices[i]
		return summary
