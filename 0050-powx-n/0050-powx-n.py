class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        a = self.myPow(x, n//2) 
        if n % 2 == 0:
            return a * a
        else:
            return a * a * x
        