class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i>=0 and digits[i]==9: #if the digit is nine assign the digit to zero and shift it by one 
            digits[i]=0
            i-=1
        if i>=0: #if the index is greater than or equal to zero then the loop hadn't been finished so just increment by one
            digits[i]+=1
        else:
            digits.insert(0,1)
        return digits