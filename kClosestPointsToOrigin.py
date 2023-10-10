import heapq
import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        priorityQueue = []
        distanceToPoint = {}

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(
                (x ** 2) + (y ** 2)
            )

            heapq.heappush(priorityQueue, distance)

            if (distanceToPoint.get(distance) == None):
                distanceToPoint[distance] = [point]
            else:
                distanceToPoint[distance].append(point)
        
        closestPoints = []
        while (len(closestPoints) < k):
            dequeueDistance = heapq.heappop(priorityQueue)
            dequeuePoints = distanceToPoint[dequeueDistance]

            closestPoints = closestPoints + dequeuePoints

        return closestPoints
        