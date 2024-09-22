class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def rec(i):
            if i == n:
                ans.append(nums[:])
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                rec(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        rec(0)
        return ans
            