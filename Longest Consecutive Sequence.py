class Solution:
    def longestConsecutive(self, num):
        pool=set(num)
        size=len(num)
        maxv=1
        for i in range(size):
            if num[i] in pool:
                counter=1
                next = num[i]-1
                while next in pool:
                    pool.remove(next)
                    counter+=1
                    next-=1
                next = num[i]+1
                while next in pool:
                    pool.remove(next)
                    counter+=1
                    next+=1
                maxv=max(maxv,counter)
        return maxv
