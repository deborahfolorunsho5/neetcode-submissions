class Solution:
    def isHappy(self, n: int) -> bool:
        
        Visited = set()

        def compute(n):
            
            res = 0

            while n > 0 :

                digit = n % 10
                res = res + digit ** 2
                n = n // 10

            return res
        
        
        while True:

            if n not in Visited:
                Visited.add(n)
            else:
                 return False

            n = compute(n)

            if n == 1:
                return True
