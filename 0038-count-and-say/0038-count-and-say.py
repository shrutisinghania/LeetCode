class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = "1"
        for _ in range (n-1):
            i = 0
            t = ''
            while i < len(s):
                c = 1
                while i < len(s) - 1 and s[i] == s[i+1]:
                    c += 1
                    i += 1
                t = t + str(c) + str(s[i])
                i += 1
            s = t
        return s