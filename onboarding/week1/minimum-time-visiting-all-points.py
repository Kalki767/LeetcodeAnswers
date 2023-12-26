class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(len(points)-1):
            x_inc = abs(points[i][0]-points[i+1][0])
            y_inc = abs(points[i][1]-points[i+1][1])
            total+= max(x_inc,y_inc) 
        return total