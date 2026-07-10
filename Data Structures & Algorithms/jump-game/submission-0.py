class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #for i in nums:#this is wrong bc it will give us the value not the index
        farthest = 0 
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True 
            # i will essentially tell you how much to canJump
            # if i is 0 and is not the las index it is False
            # else it is true