class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findMax(i, j):
            
            if dp[i][j] != -1:
                return dp[i][j]

            dir = [[0,1], [0,-1], [1,0], [-1,0]]
            max_neighbour = 0
            for x, y in dir:
                a = i + x
                b = j + y
                if not (0 <= a < m) or not (0 <= b < n):
                    continue
                if matrix[a][b] > matrix[i][j]:
                    max_neighbour = max(max_neighbour, findMax(a,b))
            dp[i][j] = 1 + max_neighbour
            return dp[i][j]

        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                max_len = max (max_len, findMax(i, j))
        
        return max_len
                