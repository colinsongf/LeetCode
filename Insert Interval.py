class Interval(object):
    """docstring for Interval"""
    def __init__(self, s=0,e=0):
        super(Interval, self).__init__()
        self.start=s
        self.end=e

class Solution:
    def insert(self,intervals,newInterval):
        for interval in intervals:
            if interval.start<=newInterval.start and newInterval.end<=interval.end:
                newInterval=None
                break
            if newInterval.start<=interval.start<=newInterval.end:
                newInterval.end=max(interval.end,newInterval.end)
            if newInterval.start<=interval.end<=newInterval.end:
                newInterval.start=min(interval.start,newInterval.start)
        #print newInterval.start,newInterval.end
        answer=[]
        for interval in intervals:
            if not newInterval:
                answer.append(interval)
            elif newInterval.start<=interval.start and interval.end<=newInterval.end:
                continue
            elif interval.end<newInterval.start:
                answer.append(interval)
            elif interval.start>newInterval.end:
                answer.append(newInterval)
                newInterval=None
                answer.append(interval)
        if newInterval:
            answer.append(newInterval)
        return answer

def dispIntervals(intervals):
    for interval in intervals:
        print '[',interval.start,',',interval.end,']',
    print

ins=Solution()

array=[Interval(1,5)]#,Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
newInterval=Interval(2,3)

newarray=ins.insert(array,newInterval)

dispIntervals(newarray)