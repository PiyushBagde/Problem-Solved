class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_row = len(matrix)
        n_col = len(matrix[0])


        z_row = []
        z_col = []

        for row  in range(n_row):
            for col in range(n_col):
                if matrix[row][col] == 0:
                    z_row.append(row)
                    z_col.append(col)

        for i in range(n_col):
            for x in z_row:
                matrix[x][i] = 0

        for i in range(n_row):
            for y in z_col:
                matrix[i][y] = 0

        
        



        