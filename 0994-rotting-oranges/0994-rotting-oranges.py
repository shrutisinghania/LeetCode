class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])
        one = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    one += 1
        
        if one == 0:
            return 0
        val = -1
        d = [[-1,0], [1,0], [0,1], [0,-1]]
        while len(q) != 0:
            s = len(q)
            while s != 0:
                i, j = q.pop(0)
                s -= 1
                for a, b in d:
                    l = i + a
                    r = j + b
                    if 0 <= l < m and 0 <= r < n and grid[l][r] == 1:
                        grid[l][r] = 2
                        one -= 1
                        q.append([l, r])
            val += 1
        if one != 0:
            return -1
        return val
        