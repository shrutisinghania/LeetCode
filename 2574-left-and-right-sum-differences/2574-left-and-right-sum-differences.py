class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for i in nums:
            right -= i
            ans.append(abs(right - left))
            left += i
        return ans
        