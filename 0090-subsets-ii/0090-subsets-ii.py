class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def rec(i, l):
            if i == n:
                res.append(l[:])
                return
            l.append(nums[i])
            rec(i+1, l)
            l.pop()
            
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
                
            rec(i+1, l)
            
        n = len(nums)
        nums.sort()
        res = []
        rec(0, [])
        return res