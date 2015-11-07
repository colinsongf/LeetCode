class Solution:
    def maxSubArray(self, array):
        size=len(array)
        record=[x for x in array]
        record[0]=array[0]
        maxvalue=record[0]
        for i in range(1,size):
            if array[i]+record[i-1]>array[i]:
                record[i]=array[i]+record[i-1]
            if record[i]>maxvalue:
                maxvalue=record[i]
        return maxvalue