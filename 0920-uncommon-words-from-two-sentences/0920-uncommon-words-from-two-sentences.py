class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = defaultdict(int)
        for i in s1.split(" "):
            d[i] += 1
        for i in s2.split(" "):
            d[i] += 1
        l = []
        for k, v in d.items():
            if v == 1:
                l.append(k)
        return l