class Solution(object):
    def findDuplicates(self, nums):
        answer = []
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
            else:
                answer.append(abs(num))
        return answer
