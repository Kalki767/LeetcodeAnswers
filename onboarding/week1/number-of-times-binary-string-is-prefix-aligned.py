class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ''' Approach
        here we are asked to check if at the index i each and every element before it is 1 and after it is 0. to check that we can check if for each index i every element before it has been changed by one. we can do that by using the prefix sum to store the sum on each step and compare it with our calculated sum at index i which is found by using arithmetic sum
        Time Complexity = O(n)
        Space Complexity = O(n)
        we can reduce the space complexity by removing the prefix sum and do the calculation at each step
        '''
        counter = 0
        prefix_sum = [flips[0]]*len(flips)
        for i in range(1,len(flips)):
            prefix_sum[i] = prefix_sum[i-1]+flips[i]
        for i in range(len(flips)):
            n = i+1
            if n*(n+1)//2 == prefix_sum[i]:
                counter+=1
        return counter