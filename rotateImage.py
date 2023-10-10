class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Tranpose matrix
        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # Switch the columns
        for col1 in range(0, len(matrix)//2):
            col2 = len(matrix) - col1 - 1
            for row in range(0, len(matrix)):
                temp = matrix[row][col1]
                matrix[row][col1] = matrix[row][col2]
                matrix[row][col2] = temp