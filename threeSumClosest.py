import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        closestTarget = sys.maxint
        closestTriple = [0, 0, 0]
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1

            while (j<k):
                currTarget = nums[i] + nums[j] + nums[k]
                if (currTarget < target):
                    if ((abs(currTarget - target) < abs(closestTarget - target))):
                        closestTarget = currTarget
                        closestTriple = [i, j, k]
                    j += 1
                else:
                    if ((abs(currTarget - target) < abs(closestTarget - target))):
                        closestTarget = currTarget
                        closestTriple = [i, j, k]
                    k -= 1
        
        return (
            nums[closestTriple[0]] +
            nums[closestTriple[1]] +
            nums[closestTriple[2]]
        )