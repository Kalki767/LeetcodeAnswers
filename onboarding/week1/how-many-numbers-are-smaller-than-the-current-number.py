class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)
        n = len(nums)
        start,index =0,0
        value = {}
        ans = [0]*n
        while index<n:
            value[nums2[index]]=index
            while index<n-1 and nums2[index]==nums2[index+1]:
                index+=1
            index+=1
        for num in range(n):
            ans[num] = value[nums[num]]
        return ans
