class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a set 
        #input is a string 
        #output is a num
        result = 0

        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i,len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #         result = max(result,len(charSet))

        # return result 
        #runtime is O(n^2) bc of the inner loop

        charSet = set()
        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                #why is s[r] alr in charsrt??
                charSet.remove(s[left])
                #in the first iteration this is checking if the first and last index have the same value 
                left += 1
                #next index
            charSet.add(s[r])
            #why???
            result = max(result,r - left + 1 )
        return result 