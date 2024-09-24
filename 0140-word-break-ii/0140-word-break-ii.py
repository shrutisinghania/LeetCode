class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> List[str]:
        def rec(l, s):
            if len(s) == 0:
                res.append(l.lstrip())
                return
            # if s in d:
            #     return d[s]
            for i in words:
                if s.startswith(i):
                    new_s = l + " " + i 
                    rec(new_s, s[len(i):])
                        # d[s] = True


        words = set(wordDict)
        d = {}
        res = []
        rec('', st)
        return res

