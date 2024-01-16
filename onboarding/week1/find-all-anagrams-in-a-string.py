class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sliding window Approach
        currentWindow = Counter(s[:len(p)])
        targetWindow = Counter(p)
        ans = []
        if targetWindow==currentWindow:
            ans.append(0)
        left,right=0,len(p)
        while right<len(s):
            if s[right] in currentWindow:
                currentWindow[s[right]]+=1
            else:
                currentWindow[s[right]]=1
            currentWindow[s[left]]-=1
            if currentWindow[s[left]]==0:
                del currentWindow[s[left]]
            if targetWindow==currentWindow:
                ans.append(left+1)
            left+=1
            right+=1
        return ans