class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''Approach:
        convert it into string to compare two elements if their sum is
        greater than another version of their sum and swap them in the sort
        function
        '''
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def compare(n1,n2):
            if n1+n2>n2+n1: #if their concaenation is greater then no swapping should occur
                return -1
            else:
                return 1
        nums = sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))