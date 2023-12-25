class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed =[]
        for i in range(1,len(nums),2):
            decompressed.extend([nums[i] for j in range(nums[i-1])])
        return decompressed