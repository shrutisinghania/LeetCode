class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = copy.deepcopy(nums)
        nums.sort()
        for ind, i in enumerate(a):
            a[ind] = nums.index(i)
        return a