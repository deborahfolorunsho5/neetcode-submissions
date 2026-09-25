class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i

        
        # for num in nums:
        #     if target - num = a number in nums
        #     then return the index of both?? 
        
    