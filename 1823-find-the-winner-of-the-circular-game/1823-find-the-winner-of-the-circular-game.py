class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i+1 for i in range(n)]
        k = k-1
        prev = 0
        while len(l) != 1 : 
            prev = (prev + k) % len(l)
            l.pop(prev)
        return l[0]