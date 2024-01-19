class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Step1: assign one pointer to the beginning of the array
        left=0

        #Step2: iterate through the array until the left pointer reaches the second last element
        while left<len(nums)-1:

            #Step3: assign another pointer right which is the left pointer incremented by one and check if the element at that pointer is bigger or not
            right = left+1
            while right<len(nums):
                if nums[left]>nums[right]:
                    nums[left],nums[right]=nums[right],nums[left]
                if nums[left]==0:
                    break
                right+=1
            left+=1
    