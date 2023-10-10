class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numIslands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if (grid[i][j] == "1"):
                    self.markIsland(grid, i, j)
                    numIslands += 1
        
        return numIslands

    def markIsland(self, grid, i, j):

        stack = [(i, j)]
        while (len(stack) > 0):
            point = stack.pop()
            currI = point[0]
            currJ = point[1]

            grid[currI][currJ] = "-1"
            for neighborI in range(currI-1, currI+2):
                for neighborJ in range(currJ-1, currJ+2):
                    checkI = (0 <= neighborI) and (neighborI < len(grid))
                    checkJ = (0 <= neighborJ) and (neighborJ < len(grid[0]))

                    if (
                        checkI and
                        checkJ and
                        (abs(currI-neighborI) + abs(currJ-neighborJ) == 1) and
                        grid[neighborI][neighborJ] == "1"
                    ):
                        print((neighborI, neighborJ))
                        stack.append((neighborI, neighborJ))