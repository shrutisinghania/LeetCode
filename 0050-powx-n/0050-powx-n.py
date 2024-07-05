class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(p, n):
            if n == 0 or p == 1:
                return 1
            r = rec(p * p, n//2)
            return r * p if n % 2 != 0 else r

        if n <= -1:
            return 1/rec(x, -n)
        return rec(x, n)