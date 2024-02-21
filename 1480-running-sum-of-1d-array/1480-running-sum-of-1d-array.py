class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        for ind, i in enumerate(nums):
            s += i
            nums[ind] = s
        return nums
            