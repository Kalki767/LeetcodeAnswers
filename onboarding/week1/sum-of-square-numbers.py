class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_root = math.floor((math.sqrt(c)))
        root = [i for i in range(square_root+1)]
        left,right = 0,len(root)-1
        while left<=right:
            value = root[left]**2+root[right]**2
            if value<c:
                left+=1
            elif value>c:
                right-=1
            else:
                return True
        return False