class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        c = 0
        while c != k:
            if i not in arr:
                c += 1
            i += 1
        return i-1