class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        c = 1
        if s[0] == '-' or s[0] == '+':
            c = -1 if s[0] == '-' else 1
            s = s[1:]
        def find(s):
            n = 0
            nos = '0123456789'
            for i in s:
                if i not in nos:
                    return n
                n = n*10 + int(i)
            return n
        
        n = find(s)*c
        if n > (2 ** 31 - 1):
            return 2 ** 31 - 1
        if n < -2 ** 31:
            return -2 ** 31
        return n
        