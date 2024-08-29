class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        def rotateDigit(xr, xc):
            val = matrix[xr][xc]
            for i in range(4):
                r = xc
                c = n - xr
                temp = matrix[r][c]
                matrix[r][c] = val
                val = temp
                xr = r
                xc = c


        for i in range((n//2)+1):
            for j in range(i, n-i):
                rotateDigit(i, j)
