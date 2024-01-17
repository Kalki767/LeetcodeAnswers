class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        '''Approach 
        first sorting the input so that we could get largest values easily
        second counting the ocurrence of each element because whenever an
        element is changed to the next largest all elements with the same 
        value should also
        third while iterating throughe the sorted input backward hold the 
        ocurrence of the current element and pass it to the next element
        fourth sum them up while iterating
        '''
        nums.sort()
        counter = Counter(nums)
        minimum = nums[0]
        index = len(nums)-1
        while index>-1 and nums[index]==nums[len(nums)-1]:
            index-=1
        if index==-1:
            return 0
        total = value = counter[nums[index+1]]
        while nums[index]>minimum:
            if nums[index]!=nums[index+1]:
                total+=value+counter[nums[index]]
                value+=counter[nums[index]]
            index-=1
        return total
        #Time Complexity = O(n)
        #Space Complexity = O(n)