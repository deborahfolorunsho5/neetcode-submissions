class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            #dont understand why it adds 1 to row 
            for col in range(row + 1, n):
                saved_value = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = saved_value

        for singleRow in matrix:
            singleRow.reverse()




        # input is a matrix of integers
        # output is another 2D matrix of integers 

        # idk how we would move the numbers in the matrix 

#         first row → last column
# last column → last row
# last row → first column
# first column → first row
# we are going to transpose 
#swap matrix[i][j] with matrix[j][i]