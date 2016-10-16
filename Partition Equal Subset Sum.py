import copy

class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 1:
            return False
        summary = sum(nums)
        if summary % 2:
            return False
        summary /= 2
        can_reach_set = set([0])
        for number in nums:
            can_reach_set_copy = copy.copy(can_reach_set)
            for s in can_reach_set_copy:
                if s + number < summary:
                    can_reach_set.add(s + number)
                if s + number == summary:
                    return True
        return False
