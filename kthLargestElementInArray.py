import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        priorityQueue = []

        for num in nums:
            heapq.heappush(priorityQueue, num)

        result = 0
        for i in range(0, len(priorityQueue) - k + 1):
            result = heapq.heappop(priorityQueue)

        return result