class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# // input is an array
# //output is a list of k numbers
# // loop through array
# // make a dict to record how many times each number appears in the array
# // return key with the highest value

        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        ordered = sorted(result.keys(), key = lambda num: result[num], reverse = True) # the sort RULE: rank each n by its count
        return ordered[:k]