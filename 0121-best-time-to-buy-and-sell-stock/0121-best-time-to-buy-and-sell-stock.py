class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ma = prices[0]
        d = 0
        for i in prices:
            if i > ma:
                ma = i
                d = max(d, ma - mi)
            if i < mi:
                mi = i
                ma = i
                d = max(d, 0)
        return d
        