class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        a = [[] for _ in range(n)]
        d = defaultdict(int)
        for i in nums:
            d[i] = d.get(i, 0) + 1

        d = sorted(d.items(), key = lambda x: -x[1])
        l = []
        for p in d[:k]:
            l.append(p[0])
            
        return l