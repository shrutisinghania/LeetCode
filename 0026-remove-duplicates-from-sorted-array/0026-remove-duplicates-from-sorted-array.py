class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        last = None
        for i in nums:
            if i == last:
                continue
            nums[c] = i
            c += 1
            last = i
        return c