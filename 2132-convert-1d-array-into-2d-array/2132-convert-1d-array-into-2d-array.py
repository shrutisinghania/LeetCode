class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        mat = []
        for i in range(m):
            mat.append(original[i*n : (i+1)* n])
        return mat