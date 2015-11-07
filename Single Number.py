class Solution(object):
    def singleNumber(self,array):
        size = len(array)
        if size==1:
            return array[0]
        number = 0
        for i in range(size):
            number ^= array[i]
        return number

ins=Solution()
print ins.singleNumber([1,2,2,3,4,5,6,4,3,6,1])