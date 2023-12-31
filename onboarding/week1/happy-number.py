class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sum_of_squares(n)
            if n==1:
                return True
        return False
    def sum_of_squares(self,n):
        output = 0
        while n:
            digit = n%10
            output+=(digit**2)
            n//=10
        return output