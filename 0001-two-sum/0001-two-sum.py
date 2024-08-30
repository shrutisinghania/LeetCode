class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind,i in enumerate(nums):
            if target - i in d.keys():
                return [ind, d[target - i]]
            d[i] = ind

