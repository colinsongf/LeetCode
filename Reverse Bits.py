class Solution:
    def reverseBits(self,n):
        ret=0
        counter=0
        while n:
            x=n&1
            ret<<=1
            ret+=x
            n=n>>1
            counter+=1
        ret<<=(32-counter)
        return ret

ins=Solution()
print ins.reverseBits(4326)
