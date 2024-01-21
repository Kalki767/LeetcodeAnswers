class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Approach: Sliding window with fixed size

        #Step1: assign two pointers to the start of the array and current vowel and max vowel variables to zero and inititalize a set containing vowels
        vowels = {'a','e','i','o','u'}
        left = right=0
        max_vowels=current_vowels=0

        #Step2: iterate through the array until the right pointer reaches it's end
        while right<len(s):

            #Step3: check if the window size is equal to k 
            if right-left==k:
                max_vowels = max(max_vowels,current_vowels)
                if s[left] in vowels:
                    current_vowels-=1
                left+=1
            else:
                if s[right] in vowels:
                    current_vowels+=1
                right+=1
        #Step4: update the max_value again 
        max_vowels = max(max_vowels,current_vowels)
        return max_vowels
        #Time Complexity: O(n)
        #Space Complexity: O(1)