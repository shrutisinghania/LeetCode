class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = nums[0]
        l, ans = 0, 0
        for i in nums:
            if i == m:
                l += 1    
            elif i > m:
                m = i
                l = 1 
                ans = 0
            else:
                l = 0
            ans = max(ans, l)
        return ans