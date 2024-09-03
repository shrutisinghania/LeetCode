class Solution:
    def getLucky(self, s: str, k: int) -> int:
        su = 0
        for c in s:
            no = ord(c) - ord('a') + 1
            su += (no % 10) + (no // 10)
        k = k-1
        while k:
            ksum = 0
            while su > 0:
                ksum += su % 10
                su = su // 10
            k -= 1
            su = ksum
        return su