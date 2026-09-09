class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:#New interval's end is before current interval's start
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:#current interval's end is before the new interval's start.
                res.append(intervals[i])
            else:#if there is overlap we pick the max and min
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval) 
        return res