class Solution(object):
    def findDisappearedNumbers(self, nums):
        answer = []
        for num in nums:
            print nums
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                answer.append(i + 1)
        return answer
