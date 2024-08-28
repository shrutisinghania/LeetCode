class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m = len(grid2)
        n = len(grid2[0])

        def bfs(q):
            d = [[-1, 0],[1, 0], [0, 1], [0, -1]]
            is_sub_island = True
            while q:
                r, c = q.pop()
                for i, j in d:
                    row = i + r
                    col = j + c
                    if 0 <= row < m and 0 <= col < n:
                        if grid2[row][col] == 1:
                            grid2[row][col] = 0
                            if grid1[row][col] != 1:
                                is_sub_island = False
                            q.append((row, col))
            return is_sub_island

        c = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    q = []
                    grid2[i][j] = 0
                    q.append((i, j))
                    if bfs(q):
                        c += 1
        return c
            




