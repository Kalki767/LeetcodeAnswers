class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        num = []
        nums1 = [x for x in nums if x>0]
        nums2 = [x for x in nums if x<0]
        for i in range(len(nums)//2):
            num.append(nums1[i])
            num.append(nums2[i])
        return num