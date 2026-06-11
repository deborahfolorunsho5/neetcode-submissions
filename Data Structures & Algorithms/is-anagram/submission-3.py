class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        return countS == countT
        
# // create dictionaries for each string 
# // loop through the string and put the letter and how many times it appreas
# // compare the dictionaries  