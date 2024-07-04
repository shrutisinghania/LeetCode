class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, i in enumerate(nums):
            try:
                if target - i in nums:
                    return [ind, nums.index(target - i, ind+1)]
            except:
                continue