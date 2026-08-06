class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        # res = 0
        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        # res = max(res, area)
        res = 0
        left = 0
        right = len(heights) -1 
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            res = max(res,area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]: 
                right -= 1
        return res