class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        val = 0
        p = 0
        for i in range(len(s) - 1, -1, -1):
            if p > d[s[i]]:
                val -= d[s[i]]
            else:
                val += d[s[i]]
            p = d[s[i]]
        return val