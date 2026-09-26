# class Solution:
#     def validPalindrome(self, s: str) -> bool:
        
#         if s == s[::-1]:
#             return True
        
#         return Falsex
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skipLeft = s[l + 1 : r + 1]   # drop the left letter
                skipRight = s[l : r]          # drop the right letter
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
# return True if EITHER one is a palindrome

        return True