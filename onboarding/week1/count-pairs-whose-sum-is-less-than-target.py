class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        '''Approach: Two pointer
        Step1: sort the input
        Step2: iterate through the input and check if the sum of right
        and left is less than target if it is then all elements inside
        will be less to so add right-left if not decrement right by 1
        '''
        nums.sort()
        total =0
        left,right = 0,len(nums)-1
        while left<right:
            if nums[left]+nums[right]>=target:
                right-=1
            else:
                total+=right-left
                left+=1
        return total
        #Time Complexity:O(nlogn)
        #Space Complexity:O(1)