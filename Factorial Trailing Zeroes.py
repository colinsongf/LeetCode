class Solution(object):
    def trailingZeroes(self,n):
        ret = 0
        while n/5:
            ret+=n/5
            n/=5
        return ret

ins=Solution()

print ins.trailingZeroes(25)