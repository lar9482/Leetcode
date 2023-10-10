class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if (x >= 0):
            
            reversedNum = 0
            while (num > 0):
                currDigit = num % 10
                reversedNum += currDigit
                reversedNum *= 10
                
                num = num / 10
            
            return reversedNum / 10 == x
        else:
            return False