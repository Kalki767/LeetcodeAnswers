class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        maximum =0
        for i in range(1,n-1):
            for j in range(1,m-1):
                value = self.sumOfHourglass(grid,i,j)
                maximum = max(value,maximum)
        return maximum
    def sumOfHourglass(self,grid: List[List[int]],i,j)->int:
        return grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]