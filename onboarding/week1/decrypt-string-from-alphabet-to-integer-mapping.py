class Solution:
    def freqAlphabets(self, s: str) -> str:
        b = ""
        i =0
        while i<len(s):
           if i+2<len(s) and s[i+2]=="#":
               total=int(s[i:i+2])
               b+=chr(ord("a") + total-1)
               i+=3
           else:
               b+=chr(ord("a")+int(s[i])-1)
               i+=1
        return b
                
        