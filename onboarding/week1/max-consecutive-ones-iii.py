class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #Approach: Sliding window with dynamic size
        #Step1: assign two pointers to the start of the array and max_ones,count of zero to 0
        left=right=0
        max_ones = count_of_zero=0

        #Step2: iterate through the array until the right pointer reaches it's end
        while right<len(nums):

            #Step3: if count of zero is less than k then check the current element and increment it by 1 and update the right pointer
            if count_of_zero<k:
                if nums[right]==0:
                    count_of_zero+=1
                right+=1

            #Step4: if the count is equal to k then check the current element if it's zero update max one and shrink the window size if not expand the window size
            else:
                if nums[right]==0:
                    max_ones = max(max_ones,right-left)
                    while count_of_zero==k:
                        if nums[left]==0:
                            count_of_zero-=1
                        left+=1
                else:
                    right+=1
        max_ones = max(max_ones,right-left)
        return max_ones
        #Time Complexity: O(n)
        #Space Complexity: O(1)