class Solution:
    def countBits(self, n: int) -> List[int]:
        # input is an int 
        # output is an array
        result = []

        for i in range(n+1):
            cal = bin(i).count("1")
            result.append(cal)

        
        return result

        # bin(input).count("1")
        # but we have to somehow put it in a list