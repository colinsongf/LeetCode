class Solution(object):
    def singleNumber(self,array):
        size = len(array)
        if size==1:
            return array[0]
        number = 0
        for i in range(size):
            number ^= array[i]
        return number
