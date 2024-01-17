class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        '''Approach: Counting sort
        first: find the maximum value to use it as the size of the new
        array
        second: sort the input using counting
        third: iterate through the sorted array and take the minimum of
        icebars the coin can buy and decrement the coin by it
        '''
        maximum = max(costs)
        count_sort = [0]*(maximum+1)
        for i in costs:
            count_sort[i]+=1
        index=total=0
        while index<(maximum+1) and coins>0:
            if count_sort[index]!=0:
                amount = min(coins//index,count_sort[index])
                total+=amount
                coins-=(amount*index)
                count_sort[index]-=amount
            index+=1
        return total
        #Time Complexity: O(n)
        #Space Complexity: O(n)