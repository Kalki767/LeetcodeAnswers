class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Approach: Sliding Window with fixed size
        #Step1: initialize a tartget dictionary that counts the ocurrence of each character in s1 and index to 0
        index =0
        len_s1,len_s2=len(s1),len(s2)
        target = Counter(s1)

        #Step2: iterate through the array until index reaches len_s2-len_s1
        while index<=len_s2-len_s1:
            
            #Step3: check if the current element is in target if not then continue the iteration
            if s2[index] not in target:
                index+=1
            
            #Step4: if it exists take a window size of len_s1 that starts at index and count occurrences of each character
            else:
                window = Counter(s2[index:index+len_s1])

                #Step5: check if the window is equal with target and return True
                if window==target:
                    return True
                index+=1
        #Step6: if nothing is returned return False
        return False
        #Time Complexity: O(n)
        #Space Complexity: O(1)