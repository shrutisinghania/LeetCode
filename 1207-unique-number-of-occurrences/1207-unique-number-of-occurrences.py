class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if a in d.keys():
                d[a] += 1
            else:
                d[a] = 0
        l = d.values()
        return len(l) == len(set(l))
        