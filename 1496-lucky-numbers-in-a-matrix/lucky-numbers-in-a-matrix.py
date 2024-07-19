class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = [min(row) for row in matrix]
        maxs = []
        res = []

        for i in range(len(matrix[0])):
            max_val = matrix[0][i]
            for j in range(len(matrix)):
                max_val = max(max_val, matrix[j][i])
            maxs.append(max_val)

        for i in mins:
            if i in maxs:
                res.append(i)
        return res

        