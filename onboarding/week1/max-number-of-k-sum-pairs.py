class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''Approach: Two Pointer
        Step1: sort the input
        Step2: assign two pointers to the first and last index and iterate
        through the array
        Step3: if their sum is equal to k move both pointers and increase
        the removed variable by 1if not moveone of the pointers 
        according to the situation
        Step4: return how many pairs you removed
        '''
        nums.sort()
        removed =0
        left,right = 0,len(nums)-1
        while left<right:
            if nums[left]+nums[right]<k:
                left+=1
            elif nums[left]+nums[right]>k:
                right-=1
            else:
                removed+=1
                left+=1
                right-=1
        return removed
        #Time Complexity:O(nlogn)
        #Space Complexity:O(1)