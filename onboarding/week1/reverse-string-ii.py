class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans =[] #creating an empty list to hold the reversed list
        n = len(s)
        for i in range(0,n,2*k): #iterating through the string to reverse it every 2k times
            if i+k<=n: #checking list index out of bound situation
                ans.extend(self.reverselist(list(s[i:i + k])))
            else: #if it is out of bounds reverse the remaining elements
                ans.extend(self.reverselist(list(s[i:])))
            if i+2*k<n: # checking the index to append the next elements
                ans.extend(list(s[i+k:i+2*k]))
            else: #if it is out of bounds append the remaining elements
                ans.extend(s[i+k:])
        return "".join(ans) #join the resulting string
    def reverselist(self,m: list): #a function to return reversed list
        m.reverse()
        return m