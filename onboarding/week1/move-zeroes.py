class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index =0
        for seek in range(len(nums)):
            if nums[seek]!=0:
                nums[index],nums[seek]=nums[seek],nums[index]
                index+=1
        
        