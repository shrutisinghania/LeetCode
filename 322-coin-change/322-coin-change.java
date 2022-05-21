class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        if (coins == null || coins.length == 0) return -1;
        
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        
        for (int coin : coins) {
            for (int c = coin; c <= amount; c++) {
                if (dp[c - coin] != Integer.MAX_VALUE) 
                    dp[c] = Math.min(dp[c], 1 + dp[c - coin]);
            }
        }
        
        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}