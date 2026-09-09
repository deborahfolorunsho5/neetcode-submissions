# # class Solution:
# #     def canJump(self, nums: List[int]) -> bool:
# #         my thought process is to access each array then use the number at that index to determine which index to go to after 
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goal = len(nums) - 1
#         for i in range(len(nums) - 2, -1, -1):
#             if i + nums[i] >= goal:
#                 goal = i
#         return goal == 0
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True