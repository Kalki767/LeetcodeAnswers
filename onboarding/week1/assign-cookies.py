class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        total=left=right=0
        while left<len(g) and right<len(s):
            if g[left]<=s[right]:
                total+=1
                left+=1
            right+=1
        return total