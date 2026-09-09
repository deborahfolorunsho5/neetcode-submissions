class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i :i[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        
        return output 
        
        # res = []
        # for i in range(len(intervals)):
        #     #loop through each index and compare the start num to the start num of the other ones if they are the same join them 
        #     #find the overlap, they cna overlap if its the same start num or end num
        #     #start num is the same
        #     #end num of indec[0] is the same as start num of index 1
        #     if interval[i][0] <= interval[i+1][0]:
        #         res= merge both numbers 
