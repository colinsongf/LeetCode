class Solution:
    def rangeBitwiseAnd(self, start,end):
        i,answer=0,0
        size=end-start+1
        while i<=32:
            bit=1<<i
            if size<(2**i)+1:
                if (start & bit) and (end & bit):
                    answer|=(1<<i)
            i+=1
        return answer

ins=Solution()

print ins.rangeBitwiseAnd(5,7)