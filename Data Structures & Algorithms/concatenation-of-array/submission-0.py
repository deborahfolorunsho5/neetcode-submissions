class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for number in nums:
            ans.append(number)

        for number in nums:
            ans.append(number)
        return ans

        #go through nums and put it in ans and then do it again? 