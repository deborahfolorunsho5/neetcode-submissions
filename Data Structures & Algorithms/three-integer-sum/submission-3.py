class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if current < 0:
                    left += 1          # sum too small → bigger number
                elif current > 0:
                    right -= 1      # sum too big → which way?
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -=1     # move both inward

        return results