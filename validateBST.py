# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        leftValues = []
        rightValues = []
        self.gatherValues(root.left, leftValues)
        self.gatherValues(root.right, rightValues)

        moreThan = self.checkMoreThan(root.val, leftValues)
        lessThan = self.checkLessThan(root.val, rightValues)
        validBST = lessThan and moreThan
    
        return validBST and self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def gatherValues(self, tree, cache):
        if tree == None:
            return
        
        cache.append(tree.val)
        self.gatherValues(tree.left, cache)
        self.gatherValues(tree.right, cache)
    
    def checkLessThan(self, val, cache):
        for i in cache:
            if val >= i:
                return False
        return True

    def checkMoreThan(self, val, cache):
        for i in cache:
            if val <= i:
                return False
        return True
        