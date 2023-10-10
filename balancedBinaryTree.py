# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True
            
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return (abs(leftDepth - rightDepth) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        maxDepth = [-1]
        self.traverse(root, 1, maxDepth)
        return maxDepth[0]
    
    def traverse(self, node, currDepth, maxDepth):
        if (node == None):
            return None

        if (currDepth > maxDepth[0]):
            maxDepth[0] = currDepth

        self.traverse(node.left, currDepth+1, maxDepth)
        self.traverse(node.right, currDepth+1, maxDepth)