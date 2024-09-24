class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def rec(st):
            if st in d:
                return d[st]
            if st == '' or st in word:
                return True
            for i in word:
                if st.startswith(i):
                    if rec(st[len(i):]):
                        d[st] = True
                        return True
            d[st] = False
            return False

        d = {}
        word = set(wordDict)
        return rec(s)
