class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y ,n = 0,x
        while n>0:
            y=(y*10) + n%10
            n//=10
        return x==y