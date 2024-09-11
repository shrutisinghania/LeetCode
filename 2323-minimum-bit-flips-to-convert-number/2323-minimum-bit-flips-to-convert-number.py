class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sb = bin(start)[2:][::-1]
        gb = bin(goal)[2:][::-1]
        m,n = len(sb), len(gb)
        c = 0
        for i in range(max(m, n)):
            a = int(sb[i]) if i < m else 0
            b = int(gb[i]) if i < n else 0
            if a != b:
                c += 1
        return c