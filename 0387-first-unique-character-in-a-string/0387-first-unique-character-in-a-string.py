class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for i, j in enumerate(s):
            if d[j] == 1:
                return i
        return -1