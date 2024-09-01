class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        mat = [[0 for _ in range(n)] for _ in range(m)]
        p = 0
        for i in range(m):
            for j in range(n):
                mat[i][j] = original[p]
                p += 1
        return mat