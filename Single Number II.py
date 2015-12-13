class Solution:
    def singleNumber(self,array):
        bitmap={}.fromkeys(range(1,33),0)
        for num in array:
            for bit in bitmap:
                if num&(1<<(bit-1)):
                    bitmap[bit]+=1
        ans=0
        for bit in range(1,32):
            if bitmap[bit]%3:
                ans+=(1<<(bit-1))
        if bitmap[32]%3:
            ans-=2**31
        return ans
