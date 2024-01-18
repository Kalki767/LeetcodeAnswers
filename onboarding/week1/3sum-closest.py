class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''Approach: Two pointers
        Step1: sort the input
        Step2: iterate through the array while calculating their sum and
        the difference between the target and the sum and updating closest
        variable when it's needed
        Step3: return closest.
        '''
        nums.sort()
        closest =0
        current_difference=0
        difference=float('inf')
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            left,right = k+1,len(nums)-1
            while left<right:
                current_sum = nums[left]+nums[right]+nums[k]
                if current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return target
                current_difference = abs(current_sum-target)
                if current_difference<=difference:
                    closest = current_sum
                    difference = current_difference
        return closest
        #Time Complexity:O(n**2)
        #Space Complexity:O(1)