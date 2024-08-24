class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color or not image:
            return image
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]

        def dfs(row, col):
            if image[row][col] == old_color:
                image[row][col] = color
                if row >= 1:
                    dfs(row - 1, col)
                if row + 1 < rows:
                    dfs(row + 1, col)
                if col >= 1:
                    dfs(row, col - 1)
                if col + 1 < cols:
                    dfs(row, col + 1)
        dfs(sr, sc)
        return image