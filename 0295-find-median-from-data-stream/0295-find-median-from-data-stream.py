class MedianFinder:

    def __init__(self):

        #two heaps

        self.small, self.large = [], [] #small is a max heap, large is a min heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        if self.small and self.large and -1 * self.small[0] > self.large[0]: #largest element in small (just pushed) bigger than smallest in large
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)
        
        #if heaps aren't evenly sized
        if len(self.small) > len(self.large) + 1: 
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, heapq.heappop(self.large) * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + self.small[0] * -1) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()