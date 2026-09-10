"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) -1 ):
            a2 = intervals[i+1].start
            b1 = intervals[i].end
            if a2 < b1:
                return False
        
        return True
# input is tuples
# output is bool
# find how it overlaps 
# if the start of index 0 is less than the start of index 1 then the end of index 0 has to be less than the end of index 1
#would we use a heap?