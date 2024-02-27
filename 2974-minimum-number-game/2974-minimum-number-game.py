class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            a = nums[i]
            nums[i] = nums[i+1]
            nums[i + 1] = a
        return nums