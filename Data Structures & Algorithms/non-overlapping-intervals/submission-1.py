class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:      # no overlap
                prevEnd = end
            else:                      # overlap
                count += 1
                prevEnd = min(prevEnd, end)
        
        return count
            #count num of overlaps
            # then see how many you need to remove
            # would we use a heap??a