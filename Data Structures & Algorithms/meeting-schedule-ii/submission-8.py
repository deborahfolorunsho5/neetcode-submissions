"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0,0
        s,e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            
            
            else:
                e += 1
                count -= 1
            res = max(res,count)
        return res

        # intervals.sort(key = lambda x: x.start)
        # numRooms = 1
        # for i in range(len(intervals)-1):
        #     a2 = intervals[i+1].start
        #     b1 = intervals[i].end
        #     if a2 < b1:
        #         numRooms +=1
        #     # elif b1 == a2:
        #     #     numRooms -= 1
        # return numRooms