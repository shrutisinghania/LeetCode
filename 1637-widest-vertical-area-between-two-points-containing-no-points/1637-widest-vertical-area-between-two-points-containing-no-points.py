class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = []
        for i in points:
            l.append(i[0])
        l.sort()
        m = 0
        for i in range(len(l)-1, 0, -1):
            m = max(m, l[i] - l[i - 1])
        return m