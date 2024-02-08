class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        for i in range(0, n):
            a.append(nums[i])
            a.append(nums[n + i])
        return a