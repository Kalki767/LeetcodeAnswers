class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = ""
        j =0
        for i in spaces:
            a+=s[j:i]
            a+=" "
            j=i
        a+=s[j:]
        return a