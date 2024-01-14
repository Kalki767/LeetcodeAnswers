class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            value = []
            for j in range(len(matrix)):
                value.append(matrix[j][i])
            transpose.append(value)
        return transpose