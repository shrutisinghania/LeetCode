class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if a not in d:
                d[a] = 0
            d[a] += 1
        l = list(d.values())
        return len(l) == len(set(l))
        