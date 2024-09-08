class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a_sub_b = (n * (n + 1))//2 - sum(nums)
        s_2 = 0
        for i in nums:
            s_2 += i * i
        a_plus_b = ((n * (n + 1) * (2*n + 1))//6 - s_2) // a_sub_b
        a = (a_sub_b + a_plus_b) // 2
        b = a - a_sub_b
        return [b, a]

        