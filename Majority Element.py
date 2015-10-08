class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        bitmap={}
        size=len(num)
        for item in num:
            if item not in bitmap:
                bitmap[item]=1
            else:
                bitmap[item]+=1
        for key in bitmap:
            if bitmap[key]>size/2:
                return key