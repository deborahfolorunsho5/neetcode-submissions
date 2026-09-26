# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         for num in numbers:
#             complement = target - num
#             if complement in numbers:
#                 return numbers[complement]
#             return list(num)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
               l += 1
        return [l + 1, r + 1]