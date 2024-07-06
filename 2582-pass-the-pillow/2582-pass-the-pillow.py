class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = time % (n-1)
        q = time // (n-1)
        i = 1 if q % 2 == 0 else -1
        if i == -1:
            return n - t
        return t + 1
# class Solution:
#     def passThePillow(self, n: int, time: int) -> int:
#         i = 1
#         while time > n-1:
#             time -= n - 1
#             i *= -1
#         if i == -1:
#             return n - time
#         return time + 1
            
            
            
            