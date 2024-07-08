class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i+1 for i in range(n)]
        k = k-1
        prev = 0
        while len(l) != 1 : 
            prev = (prev + k) % len(l)
            l.pop(prev)
        return l[0]
#     def findTheWinner(self, n: int, k: int) -> int:
#         return self.winnerHelper(n, k) + 1

#     def winnerHelper(self, n: int, k: int) -> int:
#         if n == 1:
#             return 0
#         return (self.winnerHelper(n - 1, k) + k) % n