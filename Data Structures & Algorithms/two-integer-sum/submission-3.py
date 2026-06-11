class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #for i in nums:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            #target - array[i] = needed 

            if needed in seen:
                return [seen[needed],i]

            seen[current] = i 
            # save the number that num came from in nums so we can get the index
# create a loop that goes through the array
# at index 0 it takes that value and does
# target -array[0] = num b
# then we are going to check for num b in the array and store that index 
# if its not there we keep going to the next one 