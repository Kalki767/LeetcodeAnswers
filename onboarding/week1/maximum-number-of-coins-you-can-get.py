class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''Approach: sorting
        step1: sort the input
        step2: iterate through the sorted list starting from the length of
        the list floor division by 3 to the end by incrementing 2
        '''
        piles.sort()
        n = len(piles)
        index = n//3
        maximum = 0
        while index<n:
            maximum+=piles[index]
            index+=2
        return maximum
        #Time Complexity: O(n)
        #Space Complexity: O(n)