class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        i = 1
        v = m * i
        s = 0
        while v <= n:
            s += v
            i += 1
            v = m * i
        return (n * (n + 1) // 2) - 2 * s