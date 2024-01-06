class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        matrix = {} #since in each diagonal the sum of row and column is the same we can use that as a key for the dictionary and the corresponding values as value
        for i in range(len(mat)): #traversing through the matrix row by row
            for j in range(len(mat[0])):
                value = [mat[i][j]]
                if (i+j) in matrix: #if the key exists in the dictionary extend it
                    matrix[i+j].extend(value) 
                else:
                    matrix[i+j] = value #otherwise assign a value to it
        output_matrix = []
        for key in matrix:
            if key%2==0: #reverse keys with even numbers
                matrix[key].reverse()
            output_matrix.extend(matrix[key])
        return output_matrix