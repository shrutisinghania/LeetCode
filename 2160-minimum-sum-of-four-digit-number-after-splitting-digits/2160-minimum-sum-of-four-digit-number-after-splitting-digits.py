class Solution:
    def minimumSum(self, num: int) -> int:
        l = [n for n in str(num)]
        l.sort()
        return int(l[0] + l[2]) + int(l[1] + l[3])