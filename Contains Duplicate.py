class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        size=len(nums)
        if size<=1:
            return False
        hashmap={}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num]=1
        return False