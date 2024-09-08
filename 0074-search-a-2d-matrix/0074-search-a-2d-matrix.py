class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0]) 
        s = 0
        e = m * n - 1
        while s <= e:
            mid = (s + e) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            if matrix[mid // n][mid % n] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False