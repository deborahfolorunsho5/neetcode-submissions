class Solution:
    def findMin(self, nums: List[int]) -> int:
        #search array and find the pivot 
        result = nums[0]
        left = 0
        right = len(nums) - 1 

        while left <= right:#what if its the same element 
            #checks when the window is sorted 
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break 


            mid = (left + right) // 2

            result = min(result,nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
        return result