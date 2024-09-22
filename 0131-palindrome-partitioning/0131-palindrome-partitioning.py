class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def rec(i, l):
            if i == n:
                res.append(l[:])
                return
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    l.append(s[i:j+1])
                    rec(j+1, l)
                    l.pop()
        res = []
        rec(0,[])
        return res
