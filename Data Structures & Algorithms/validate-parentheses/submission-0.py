class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack to check if the brackets are present 
        #create a dict so we know what actually matches 
        stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False

                if pairs[stack[-1]] != char:
                    # stack[-1] is the top char on the stack
                    #so get that and then take the pair of that and compare to char
                    return False

                stack.pop()

        return len(stack) == 0
# // go through the string 
# for ever ({[ it should have a corresponding closing 
# so go through it then to find a closing one 
