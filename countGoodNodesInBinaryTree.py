import copy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        solution = [0]
        self.traverseTree(root, [], solution)

        return solution[0]

    def traverseTree(self, node, seenVals, solution):
        if (node == None):
            return
        
        isGood = True
        for seenVal in seenVals:
            if seenVal > node.val:
                isGood = False
        if (isGood):
            solution[0] += 1

        self.traverseTree(node.left, seenVals + [node.val], solution)
        self.traverseTree(node.right, seenVals + [node.val], solution)