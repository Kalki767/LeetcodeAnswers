class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Approach: Two pointers
        #Step1: assign an index to the start of the array
        index =0

        #Step2: iterate through the array while checking if the current element is differenct from val if it's swap it with index
        for seek in range(len(nums)):
            if nums[seek]!=val:
                nums[index],nums[seek]=nums[seek],nums[index]
                index+=1
        return index
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
