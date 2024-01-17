class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''Approach: Two pointers
        Step1: create a list of only alphanumeric characters
        Step2: compare each elements starting from the first index using
        two pointers
        '''
        word = []
        for i in s:
            if i.isalpha():
                word.append(i.lower())
            elif i.isdigit():
                word.append(i)
        left,right = 0,len(word)-1
        while left<=right:
            if word[left]!=word[right]:
                return False
            left+=1
            right-=1
        return True
        #Time Complexity:O(n)
        #Space Complexity:O(n)