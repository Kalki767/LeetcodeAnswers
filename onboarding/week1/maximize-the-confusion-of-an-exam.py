class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #Approach: Sliding Window
        #Step1: assign two pointers to the start of the array and other variables
        left=right=0
        n = len(answerKey)
        max_True=max_False=0
        count_False=count_True=0

        #Step2: iterate through the array until the right reaches the end
        while right<n:
            #Step3: check if count_of_False is less than k and increment it by 1 if the current element is F
            if count_False<k:
                if answerKey[right]=='F':
                    count_False+=1
                right+=1
            #Step4: if not then check if the current element is F if it is update the max if not continue iterating
            else:
                if answerKey[right]=='F':
                    max_True = max(max_True,right-left)
                    while count_False==k:
                        if answerKey[left]=='F':
                            count_False-=1
                        left+=1
                else:
                    right+=1
        max_True = max(max_True,right-left)
        #Step5: assign the pointers to the start again
        left=right=0

        #Step6: do the same procedure you did for True consecutives
        while right<n:
            #Step3: check if count_of_True is less than k and increment it by 1 if the current element is T
            if count_True<k:
                if answerKey[right]=='T':
                    count_True+=1
                right+=1
            #Step4: if not then check if the current element is T if it is update the max if not continue iterating
            else:
                if answerKey[right]=='T':
                    max_False = max(max_False,right-left)
                    while count_True==k:
                        if answerKey[left]=='T':
                            count_True-=1
                        left+=1
                else:
                    right+=1
        max_False = max(max_False,right-left)
        #Step5: return the maximum of the two values
        return max(max_True,max_False)