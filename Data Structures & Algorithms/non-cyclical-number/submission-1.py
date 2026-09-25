class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while n not in visit:
            visit.add(n)
            n = self. sumOfSquares(n)
            if n == 1:
                return True
            if n in visit and n != 1:
                return False
        return False
            

    def sumOfSquares(self, n:int) -> int:

        output = 0
        while n != 0:
            digit = n % 10
            digit = digit ** 2
            output += digit 
            n = n // 10
        return output

        # visited = set()

        # def helperfun(n):
        #     total = 0
        #     while n > 0:
        #         firstNum = n % 10
        #         total += firstNum ** 2
        #         n = n // 10
        #     return total

        # while n != 1 and n not in visited:
        #     visited.add(n)
        #     n = helperfun(n)

        # return n == 1