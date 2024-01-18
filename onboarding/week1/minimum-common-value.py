class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        '''Approach: Two pointers
        Step1: assign two pointers to the begining of the array
        Step2: iterate through the lists while checking the two elements
        match or not if they do return the number otherwise continue 
        iterating
        Step3: if nothing is returned return -1
        '''
        left=right=0
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums1[left]>nums2[right]:
                right+=1
            else:
                return nums1[left]
        return -1
        #Time Complexity:O(n)
        #Space Complexity:O(1)