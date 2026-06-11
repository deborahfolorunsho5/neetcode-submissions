class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set();

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        

# create a set 
# put the values of the array inside the list and check for duplicates 