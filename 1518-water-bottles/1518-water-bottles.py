class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s = 0
        while numBottles >= numExchange:
            q = numBottles // numExchange
            s += q * numExchange
            numBottles = (numBottles % numExchange) + q
        return s + numBottles