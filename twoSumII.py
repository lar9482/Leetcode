class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ptr1 = 0
        ptr2 = len(numbers)-1

        while (ptr1 < ptr2):
            currTarget = numbers[ptr1] + numbers[ptr2]
            if (currTarget < target):
                ptr1 += 1
            elif (target < currTarget):
                ptr2 -= 1
            elif (target == currTarget):
                return [ptr1+1, ptr2+1]
        
        return [ptr1+1, ptr2+1]