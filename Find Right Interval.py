# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def minRight(end, intervals):
    head, rear = 0, len(intervals)
    while head < rear:
        mid = (head + rear) >> 1
        if intervals[mid].start >= end:
            if mid == head:
                return mid
            if intervals[mid - 1].start >= end:
                rear = mid
            else:
                return mid
        else:
            head = mid + 1
    return -1

class Solution(object):
    def findRightInterval(self, intervals):
        mydict = {}
        for i, interval in enumerate(intervals):
            mydict[interval] = i
        intervals.sort(key = lambda x: x.start)
        answer = [-1 for i in range(len(intervals))]
        for interval in intervals:
            i = minRight(interval.end, intervals)
            myanswer = -1 if i == -1 else mydict[intervals[i]]
            my_pos = mydict[interval]
            answer[my_pos] = myanswer
        return answer
