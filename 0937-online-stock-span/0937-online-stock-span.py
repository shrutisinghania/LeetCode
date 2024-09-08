class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price: int) -> int:
        span = 0
        while self.s and self.s[-1][0] <= price:
            span += self.s.pop(-1)[1]
        self.s.append((price, span + 1))
        return span+1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)