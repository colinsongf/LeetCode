class Interval(object):
    """docstring for Interval"""
    def __init__(self, s=0,e=0):
        super(Interval, self).__init__()
        self.start=s
        self.end=e

class Solution:
    def merge(self,intervals):
        size=len(intervals)
        if size<1:
            return intervals
        intervals.sort(key=lambda x:x.start)
        answer=[intervals[0]]
        currentend=intervals[0].end
        for interval in intervals[1:]:
            if interval.start<=currentend and interval.end>currentend:
                answer[-1].end=interval.end
                currentend=interval.end
            elif interval.start>currentend:
                answer.append(interval)
                currentend=interval.end
        return answer

ins=Solution()
array=[Interval(8,10),Interval(1,3),Interval(15,18),Interval(2,6)]
answer=ins.merge(array)

for ans in answer:
    print ans.start,ans.end