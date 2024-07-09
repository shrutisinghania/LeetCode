class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        c = 1
        l = []
        for ar, ct in customers:
            if ar > c:
                c = ar
            c = c + ct
            l.append(c - ar)
        return sum(l)/len(l)