class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        for i in range(1, n + 1):
            l.append(i)
        k = k-1
        prev = 0
        while len(l) != 1 : 
            prev = (prev + k) % len(l)
            l.pop(prev)
        return l[0]