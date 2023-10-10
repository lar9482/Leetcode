"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        orderList = []
        self.dfs(root, orderList, 0)

        return orderList

    def dfs(self, treeNode, orderList, depth):
        if (treeNode == None):
            return

        if depth == len(orderList):
            orderList.append([treeNode.val])
        else:
            orderList[depth].append(treeNode.val)

        for childNode in treeNode.children:
            self.dfs(childNode, orderList, depth+1)