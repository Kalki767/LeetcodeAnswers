class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''Approach: two pointers
        Step1: sort the input
        Step2: iterate through the array once using an outer for loop
        Step3: check if the current element is the same as before and if
        it is skip it.
        Step4: use the current element multiplied by -1 as the target to
        be found by the sum of two numbers
        Step5: use two pointers approach to find two elemnts whose sum is
        equal to the target
        Step6: when those elements are found check if the next elements is
        the same as before to avoid duplicates
        Step7: append the 3 elements whose sum is equal to 0
        Step8: return the array containing elements
        '''
        nums.sort()
        triplets = []
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1] :
                continue
            target = -1*nums[k]
            left,right = k+1,len(nums)-1
            while left<right:
                if nums[left]+nums[right]<target:
                    left+=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    triplets.append([nums[k],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return triplets
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)