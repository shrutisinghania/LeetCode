class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n != 1:
            if n% 2 == 0:
                m += n//2
                n = n//2
            else:
                a = (n-1)//2
                m += a
                n = a + 1
        return m
        