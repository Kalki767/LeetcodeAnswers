class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        i,j=0,0
        n,m = len(word1),len(word2)
        while i<n and j<m:
            word3+=word1[i]
            word3+=word2[j]
            i+=1
            j+=1
        if i<n:
            word3+=word1[i:]
        elif j<m:
            word3+=word2[j:]
        return word3