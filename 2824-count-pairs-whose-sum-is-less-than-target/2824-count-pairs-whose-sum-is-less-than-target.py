class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        s = 0
        for ind, i in enumerate(nums):
            t = target - i
            for j in range(ind + 1, len(nums)):
                if nums[j] < t:
                    s += 1
                    
        return s
