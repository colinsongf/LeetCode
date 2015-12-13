class Limit:
    def __init__(self,start):
        self.start = start
        self.end = start
    def toStr(self):
        return str(self.start) if self.start == self.end else str(self.start) + '->' + str(self.end)

class Solution:
    def summaryRanges(self, nums):
        answer = []
        if not nums:return answer
        prevlimit = Limit(nums[0])
        for num in nums[1:]:
            if num == prevlimit.end + 1:
                prevlimit.end += 1
            else:
                answer.append(prevlimit.toStr())
                prevlimit = Limit(num)
        answer.append(prevlimit.toStr())
        return answer
