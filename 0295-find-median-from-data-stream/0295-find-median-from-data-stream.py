class MedianFinder:

    def __init__(self):
        self.max_1 = []
        self.min_2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_1, -num)
        heapq.heappush(self.min_2, -heapq.heappop(self.max_1))
        if len(self.max_1) < len(self.min_2):
            no = heapq.heappop(self.min_2)
            heapq.heappush(self.max_1, -no) 
        # print(self.min_2, self.max_1)

    def findMedian(self) -> float:        
        if len(self.max_1) == len(self.min_2):
            return (self.min_2[0] - self.max_1[0]) / 2
        return -self.max_1[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()