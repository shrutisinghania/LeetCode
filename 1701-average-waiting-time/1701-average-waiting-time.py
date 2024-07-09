class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        c = 1
        l = 0
        for ar, ct in customers:
            if ar > c:
                c = ar
            c = c + ct
            l += c - ar
        return l /len(customers)