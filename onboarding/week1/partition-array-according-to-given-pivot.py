class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1 = [x for x in nums if x<pivot]
        nums2 = [x for x in nums if x==pivot]
        nums3 = [x for x in nums if x>pivot]
        nums2.extend(nums3)
        nums1.extend(nums2)
        return nums1