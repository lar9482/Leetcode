class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        results = set()
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1

            while (j<k):
                target = nums[i] + nums[j] + nums[k]
                if (target < 0):
                    j += 1
                elif (0 < target):
                    k -= 1
                elif (target == 0):
                    results.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
        
        return results