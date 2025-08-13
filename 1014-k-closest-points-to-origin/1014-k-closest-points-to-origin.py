class Solution(object):
    def kClosest(self, points, k):
        
        def distance(point):
            return sqrt((point[0])**2 + (point[1])**2)

        heap = []

        for point in points:
            heapq.heappush(heap, (distance(point) * -1, point))
            if (len(heap) == (k + 1)):
                heapq.heappop(heap)
            
        heap = [p[1] for p in heap]
        return heap