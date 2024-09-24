class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> List[str]:
        def rec(s):
            if s in d:
                return d[s]
            
            if not s:
                return [""]
            res = []
            for i in words:
                if s.startswith(i):
                    a = rec(s[len(i):])
                    for f in a:
                        p = i + " " + f 
                        res.append(p.rstrip())
            d[s] = res
            return res


        words = set(wordDict)
        d = {}      
        return rec(st)

