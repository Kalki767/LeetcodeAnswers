class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area =0
        left,right = 0,len(height)-1
        while left<right:
            current_area = (right-left)*min(height[left],height[right])
            if min(height[left],height[right])==height[left]:
                left+=1
            else:
                right-=1
            Area = max(Area,current_area)
        return Area