class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if not nums:
                return res
            n = target // k
            if n < nums[0] or n > nums[-1]:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    for j in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + j)
            return res
            
            
        def twoSum (nums, target):
            res = []
            l = 0
            r = len(nums) - 1
            while l<r:
                if nums[l] + nums[r] > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                elif nums[l] + nums[r] < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                else:
                    res.append([nums[l],nums[r]])
                    l += 1
                    r -= 1
            return res
            
        nums.sort()
        return kSum(nums, target, 4)
        