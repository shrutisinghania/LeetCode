class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        def checkTime(m):
            c = 0
            for p in piles:
                c += p//m
                if p % m != 0:
                    c += 1
            if c <= h:
                return True
            return False
        
        while (l < r):
            m = l + (r - l)//2
            if checkTime(m):
                r = m
            else:
                l = m + 1
        return l