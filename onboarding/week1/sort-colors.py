class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using selection sort to sort the array
        n = len(nums)
        for i in range(n):
            min_indx = i
            for j in range(i+1,n):
                if nums[j]<nums[min_indx]:
                    min_indx = j
            nums[min_indx],nums[i] = nums[i],nums[min_indx]
        