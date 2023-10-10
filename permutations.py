import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = []

        self.dfs(len(nums)-1, 0, solutions, nums)
        
        return solutions

    def dfs(self, length, i, solutions, subSolution):
        if (i == length):
            solutions.append(
                copy.deepcopy(subSolution)
            )
            return

        for j in range(i, length+1):
            newSolution = copy.deepcopy(subSolution)
            temp = newSolution[i]
            newSolution[i] = newSolution[j]
            newSolution[j] = temp

            self.dfs(length, i+1, solutions, newSolution) 
        
        