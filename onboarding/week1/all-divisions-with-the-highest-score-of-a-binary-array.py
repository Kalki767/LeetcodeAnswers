class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i =0
        count_of_one = nums.count(1)
        nums_left =0
        nums_right =count_of_one
        d = [nums_right+nums_left]
        while i<n:
            if nums[i]==0:
                nums_left+=1
            else:
                count_of_one-=1
                nums_right = count_of_one
            d.append(nums_right+nums_left)
            i+=1
        maximum = max(d)
        ans = []
        for num in range(n+1):
            if d[num]==maximum:
                ans.append(num)
        return ans