class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j=0,n
        a = []
        while i<n and j<2*n:
            a.append(nums[i])
            a.append(nums[j])
            i+=1
            j+=1
        return a