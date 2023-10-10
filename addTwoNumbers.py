# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultList = None
        currNode = None

        carry = 0
        while (l1 != None and l2 != None):
            currNum = l1.val + l2.val + carry

            digit = currNum % 10
            carry = int(currNum / 10)

            (resultList, currNode) = self.appendNode(digit, resultList, currNode)

            l1 = l1.next
            l2 = l2.next

        while (l1 != None):
            currNum = l1.val + carry

            digit = currNum % 10
            carry = int(currNum / 10)

            (resultList, currNode) = self.appendNode(digit, resultList, currNode)

            l1 = l1.next

        while (l2 != None):
            currNum = l2.val + carry

            digit = currNum % 10
            carry = int(currNum / 10)

            (resultList, currNode) = self.appendNode(digit, resultList, currNode)

            l2 = l2.next

        if carry != 0:
            (resultList, currNode) = self.appendNode(carry, resultList, currNode)
        
        return resultList

    def appendNode(self, val, resultList, currNode):
        if resultList == None:
            resultList = ListNode(val, None)
            currNode = resultList

        else:
            newNode = ListNode(val, None)
            currNode.next = newNode
            currNode = newNode
        
        return (resultList, currNode)