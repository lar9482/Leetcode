# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if (root == None):
            return False

        return (
            self.isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
    
    def isSameTree(self, p, q):

        if (p == None and q == None):
            return True
        
        elif(p != None and q != None):
            return (
                p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
            )

        else:
            return False