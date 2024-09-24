class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        l = 0
        r = n
        m = min(height[l], height[r]) * n
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
            n -= 1
            m = max(m, min(height[l], height[r]) * n)
        return m