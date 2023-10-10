import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        self.dfs(candidates, target, solutions, [])

        return solutions
        
    def dfs(self, candidates, target, solutions, subSolution):
        sumSolution = sum(subSolution)
        if (sumSolution > target):
            return
        elif (sumSolution == target):

            solutions.append(copy.deepcopy(subSolution))
            return

        for num in candidates:
            if (len(subSolution) == 0 or num >= subSolution[len(subSolution) - 1]):
                self.dfs(candidates, target, solutions, subSolution + [num])