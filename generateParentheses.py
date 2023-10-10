class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solutions = []

        self.dfs(solutions, ['(', 1, 0], n)
        
        return solutions
    
    def dfs(self, solutions, subSolutionGroup, n):

        subSolution = subSolutionGroup[0]
        numLeft = subSolutionGroup[1]
        numRight = subSolutionGroup[2]

        if (numLeft == n):
            for i in range(0, n-numRight):
                subSolution += ')'
            solutions.append(subSolution)
            return

        self.dfs(solutions, [subSolution + '(', numLeft+1, numRight], n)

        if (numRight < numLeft):
            self.dfs(solutions, [subSolution + ')', numLeft, numRight+1], n)