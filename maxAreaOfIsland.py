class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if (grid[i][j] == 1):
                    area = self.markIsland(grid, i, j)
                    maxArea = max(maxArea, area)

        return maxArea

    def markIsland(self, grid, i, j):
        stack = [(i, j)]
        area = 0
        while (len(stack) > 0):
            point = stack.pop()
            currI = point[0]
            currJ = point[1]

            if (grid[currI][currJ] == 1):
                area += 1

            grid[currI][currJ] = -1

            possibleNeighbors = [
                (currI-1, currJ),
                (currI+1, currJ),
                (currI, currJ-1),
                (currI, currJ+1)
            ]
            for possibleNeighbor in possibleNeighbors:
                possI = possibleNeighbor[0]
                possJ = possibleNeighbor[1]

                checkI = (0 <= possI) and (possI < len(grid))
                checkJ = (0 <= possJ) and (possJ < len(grid[0]))

                if (checkI and checkJ and grid[possI][possJ] == 1):
                    stack.append((possI, possJ))
        

        return area