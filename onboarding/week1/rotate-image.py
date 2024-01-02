class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i =0
        while i<len(matrix): #traversing through the matrix
            j=i #keeping track of our pointer
            while j<len(matrix[i]):
                if i!=j: #checking if the two pointers are equal
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #swapping rows and columns
                j+=1
            i+=1
        for mat in matrix: #reversing each list in the matrix
            mat.reverse()
        