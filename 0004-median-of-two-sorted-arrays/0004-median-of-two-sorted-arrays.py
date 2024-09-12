class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        v = (n // 2) + 1
        find = False
        if n % 2 == 0:
            find = True
        prev, curr = float('-inf'), float('-inf')
        i, j, c = 0, 0,0
        while c < v:
            if i >= n1:
                prev = curr
                curr = nums2[j]
                j += 1
            elif j >= n2:
                prev = curr
                curr = nums1[i]
                i += 1

            elif nums1[i] <= nums2[j]:
                prev = curr
                curr = nums1[i]
                i += 1
            else:
                prev = curr
                curr = nums2[j]
                j += 1

            c += 1
        if find:
            return (prev + curr) / 2
        return curr