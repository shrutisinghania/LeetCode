class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0

        def bfs(i, j):
            q= []
            q.append((i, j))
            grid[i][j] = '0'
            f = [[0, 1],[0, -1], [1, 0], [-1, 0]]
            while q:
                i, j =q.pop(0)
                for a, b in f:
                    r = i+a
                    c = j+b
                    if  0 <= r < m and 0<= c < n and grid[r][c] == '1':
                        q.append((r, c))
                        grid[r][c] = '0'


        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    c += 1
                    bfs(i, j)

        return c