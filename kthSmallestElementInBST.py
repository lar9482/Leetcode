import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return 0

        priorityQueue = []
        self.gatherValues(root, priorityQueue)

        result = 0
        for i in range(0, k):
            result = heapq.heappop(priorityQueue)

        return result

    def gatherValues(self, tree, priorityQueue):
        
        queue = [tree]
        while (len(queue) > 0):
            node = queue.pop(0)
            heapq.heappush(priorityQueue, node.val)
            
            if node.left != None:
                queue.append(node.left)
            
            if node.right != None:
                queue.append(node.right)