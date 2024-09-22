class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        m = 0  
        n = len(workerTimes)
        q = []
        for i in range(n):
            heapq.heappush(q, [workerTimes[i], workerTimes[i], 1])
        while mountainHeight > 0:
            s, i, c = heapq.heappop(q)
            m = max(m, s)
            s += (c+1) * i
            mountainHeight -= 1
            heapq.heappush(q, [s , i, c+1])               
        return m


