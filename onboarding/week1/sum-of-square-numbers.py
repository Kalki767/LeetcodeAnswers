class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_root = math.ceil((math.sqrt(c)))
        left,right = 0,square_root
        while left<=right:
            value = left**2+right**2
            if value<c:
                left+=1
            elif value>c:
                right-=1
            else:
                return True
        return False