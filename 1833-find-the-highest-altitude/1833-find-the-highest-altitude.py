class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        s = 0
        for i in gain:
            s += i
            m = max(s, m)
        return m