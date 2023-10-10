import copy

class Solution(object):

    def __init__(self):
        self.subset = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subset = []
        self.dfs(nums, 0, subset, [])
        
        return subset

    def dfs(self, nums, i, subset, currSubset):

        if (i == len(nums)):
            subset.append(copy.deepcopy(currSubset))
            return 
            
        currSubset.append(nums[i])
        self.dfs(nums, i+1, subset, currSubset)

        currSubset.remove(nums[i])
        self.dfs(nums, i+1, subset, currSubset)
        