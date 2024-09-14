class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<= 2:
            return max(nums)
        prev1, prev2 = 0,0  
        for i in nums:
            temp = prev1
            prev1 = max(i +  prev2, prev1)
            prev2 = temp
        return prev1