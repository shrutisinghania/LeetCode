class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0], profit = 0;
        for (int p : prices)
        {
            if (p < min)
            {
                min = p;
                continue;
            }
            profit = Math.max (profit + p - min, profit);
            min = p;
        }
        return profit;
    }
}