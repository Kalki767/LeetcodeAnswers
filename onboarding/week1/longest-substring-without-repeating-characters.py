class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Step1: assign two pointers to the beginning of the array and a dictionary to count occurrences
        window = defaultdict(int)
        left=right=0
        max_length=0

        #Step2: iterate through the list and add the current element in the dictionary
        while right<len(s):
            window[s[right]]+=1

            #Step3: check if the value of that element is greater than 1 and shrink the window by 1 until the value becomes equal to 1
            while window[s[right]]>1:
                window[s[left]]-=1
                left+=1
            #Step4: now we have unique elements we take the maximum length
            max_length = max(max_length,right-left+1)
            right+=1
        return max_length
