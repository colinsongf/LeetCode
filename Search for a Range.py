class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, array, target):
        size=len(array)
        hsp,rsp=0,size-1
        while hsp<=rsp:
            if array[hsp]<target:
                hsp+=1
            elif array[hsp]>target:
                return [-1,-1]
            if array[rsp]>target:
                rsp-=1
            elif array[rsp]<target:
                return [-1,-1]
            if array[hsp]==array[rsp] and array[rsp]==target:
                return [hsp,rsp]
        return [-1,-1]       