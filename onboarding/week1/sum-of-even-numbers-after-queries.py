class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_of_even = 0
        for i in nums:
            if i%2==0:
                sum_of_even+=i
        for i in queries:
            index = i[1]
            value = i[0]
            if nums[index]%2!=0 and value%2!=0:
                sum_of_even+=nums[index]+value
            elif nums[index]%2==0 and value%2==0:
                sum_of_even+=value
            elif nums[index]%2==0 and value%2!=0:
                sum_of_even-=nums[index]
            nums[index] =nums[index]+ value
            ans.append(sum_of_even)
        return ans