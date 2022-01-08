class Solution {
    public int cherryPickup(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][][] dp = new int[m][n][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++)
                    dp[i][j][k] = -1;
            }
        }
        return dp(0, 0, n - 1, grid, dp);
    }

    private int dp(int r, int c1, int c2, int[][] grid, int[][][] dp) {
        if (c1 < 0 || c1 >= grid[0].length || c2 < 0 || c2 >= grid[0].length)
            return 0;
        if (dp[r][c1][c2] != -1) 
            return dp[r][c1][c2];
        int result = 0;
        result += grid[r][c1];
        if (c1 != c2)
            result += grid[r][c2];
        if (r != grid.length - 1) {
            int max = 0;
            for (int nc1 = c1 - 1; nc1 <= c1 + 1; nc1++) {
                for (int nc2 = c2 - 1; nc2 <= c2 + 1; nc2++)
                    max = Math.max(max, dp(r + 1, nc1, nc2, grid, dp));
            }
            result += max;
        }
        dp[r][c1][c2] = result;
        return result;
    }
}