class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for letter in s:
            if letter.isalnum():
                cleaned += letter.lower()
        
        if cleaned == cleaned[::-1]:
            palindrome = True
        else:
            palindrome = False
        return palindrome
        # copy s 
        # s[::-1]
        # compare s and s[::-1]
        # if equal then true otherwise false