class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = []
        maxs = []
        res = []
        for i in range(len(matrix)):
            min_val = matrix[i][0]
            for j in range(len(matrix[0])):
                if matrix[i][j] < min_val:  
                    min_val = matrix[i][j]
            mins.append(min_val)


        for i in range(len(matrix[0])):
            max_val = matrix[0][i]
            for j in range(len(matrix)):
                if matrix[j][i] > max_val:
                    max_val = matrix[j][i]
            maxs.append(max_val)
        
        for i in mins:
            if i in maxs:
                res.append(i)
        return res




                

            

        