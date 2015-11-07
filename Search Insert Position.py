class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, array, target):
        size=len(array)
        pos=0
        for item in array:
            if target>item:
                pos+=1
            else:
                break
        return pos