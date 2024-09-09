class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = 0
        c2 = 0   
        n1 = nums[0]
        n2 = nums[0]
        for no in nums:
            if no == n1:
                c1 += 1
            elif no == n2:
                c2 += 1
            elif c1 == 0:
                c1 += 1
                n1 = no
            elif c2 == 0:
                c2 += 1
                n2 = no
            else:
                c1 -= 1
                c2 -= 1
        
        res = []
        c1 = 0
        c2 = 0
        for no in nums:
            if n1 == no:
                c1 += 1
            elif n2 == no:
                c2 += 1
        n = len(nums)
        n = n//3
        print(n1, n2, c1, c2)
        if c1 > n:
            res.append(n1)
        if c2 > n:
            res.append(n2)
        return res
    

