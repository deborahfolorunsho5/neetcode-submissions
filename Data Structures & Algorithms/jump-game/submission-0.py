# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         my thought process is to access each array then use the number at that index to determine which index to go to after 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0