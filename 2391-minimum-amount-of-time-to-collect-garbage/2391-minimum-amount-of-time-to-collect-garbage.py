class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        d = {'P': 0, 'G':0, 'M':0}
        t = 0
        for ind, i in enumerate(garbage):
            for c in i:
                t += sum(travel[d[c]: ind]) + 1
                d[c] = ind
        return t