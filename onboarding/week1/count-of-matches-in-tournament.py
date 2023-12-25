class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches =0
        while n>1:
            if n%2==0:
                matches+=(n//2)
            else:
                matches+=(n//2)+1
            n//=2
        return matches