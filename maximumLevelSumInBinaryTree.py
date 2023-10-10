# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        levelSums = {}
        queue = [(root, 1)]

        while (len(queue) > 0):
            nodeAndDepth = queue.pop(0)

            node = nodeAndDepth[0]
            level = nodeAndDepth[1]

            if (levelSums.get(level) == None):
                levelSums[level] = node.val
            else:
                levelSums[level] += node.val

            if (node.left != None):
                queue.append((node.left, level+1))

            if (node.right != None):
                queue.append((node.right, level+1))

        maxLevel = -1
        maxSum = -10 ** 13
        
        for level in list(levelSums.keys()):
            if (levelSums[level] > maxSum):
                maxLevel = level
                maxSum = levelSums[level]

        return maxLevel