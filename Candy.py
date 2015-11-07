class Solution:
    def candy(self, ratings):
        size=len(ratings)
        if size<=1:
            return size
        candys=[1 for x in range(size)]
        for i in range(1,size):
            if ratings[i]>ratings[i-1]:
                candys[i]=candys[i-1]+1
        for i in range(size-2,-1,-1):
            if ratings[i]>ratings[i+1] and candys[i]<=candys[i+1]:
                candys[i]=candys[i+1]+1
        return sum(candys)

ins=Solution()
print ins.candy([1,2,2])