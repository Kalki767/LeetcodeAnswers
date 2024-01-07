class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set() #creating a set to store visited indexes
        diagonal_sum = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i==j or i+j==n-1: #if i==j then it's in primary diagonal and if i+j==n-1 it's in secondary diagonal
                    t = (i,j)
                    if t not in visited: #if it's already visited skip it
                        visited.add(t)
                        diagonal_sum+=mat[i][j]
        return diagonal_sum
        # Time Complexity = O(n**2)
        # Space Complexity = O(n)