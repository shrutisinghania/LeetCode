class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        e = nums[0]
        for i in nums:
            if c == 0:
                e = i
            if i == e:
                c += 1
            else:
                c -= 1
        return e
