# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root == None):
            return None
            
        queue = [(root, 1)]
        seenDepths = {}
        result = []

        while (len(queue) > 0):
            nodeAndDepth = queue.pop(0)

            node = nodeAndDepth[0]
            depth = nodeAndDepth[1]

            if (seenDepths.get(depth) == None):
                seenDepths[depth] = depth
                result.append(node.val)

            if (node.right != None):
                queue.append((node.right, depth + 1))
            
            if (node.left != None):
                queue.append((node.left, depth + 1))
        
        return result