class Solution:
    def largestGoodInteger(self, num: str) -> str:
        value = 0
        index=-1
        for i in range(0,len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                current =int(num[i:i+3])
                if current>=value:
                   index=i
                   value = current
        if index==-1:
            return ""
        else:
            return num[index:index+3]