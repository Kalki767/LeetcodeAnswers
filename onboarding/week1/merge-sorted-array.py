class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        left,right = m-1,n-1
        while left>=0 and right>=0:
            if nums1[left]>=nums2[right]:
                nums1[index]=nums1[left]
                left-=1
            else:
                nums1[index]=nums2[right]
                right-=1
            index-=1
        while left>=0:
            nums1[index]=nums1[left]
            left-=1
            index-=1
        while right>=0:
            nums1[index]=nums2[right]
            right-=1
            index-=1
