class Solution {
    public int maxProfit(int[] prices) {
        int min = 0, maxprofit = 0;
        for(int i = 0; i < prices.length; i++)
        {
            if(prices[i] - prices[min] > maxprofit)
                maxprofit = prices[i] - prices[min];
            if(prices[i] < prices[min])
                min = i;
        }
        return maxprofit;
    }
}