class Solution:
    def fib(self, n: int) -> int:
        def find(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if f[n] != -1:
                return f[n]
            f[n] = self.fib(n-1) + self.fib(n-2)
            return f[n]
        f = [-1] * (n+1)
        return find(n)