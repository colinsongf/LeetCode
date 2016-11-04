# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def mycmp(interval1, interval2):
    if interval1.end == interval2.end:
        return interval1.start - interval2.start
    return interval1.end - interval2.end

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) <= 1:
            return 0
        intervals.sort(cmp = mycmp)
        current_end = -2**31
        counter = 0
        for interval in intervals:
            if interval.start >= current_end:
                current_end = interval.end
            else:
                counter += 1
        return counter
