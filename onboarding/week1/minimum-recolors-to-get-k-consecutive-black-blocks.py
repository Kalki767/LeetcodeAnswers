class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #Approach: Sliding Window with fixed size k
        #Step1: count the number of whites for the first k consecutive elements
        count_of_white=0
        for index in range(k):
            if blocks[index]=='W':
                count_of_white+=1
        
        #Step2: assign count of white to min white and iterate through blocks starting from k to the end while shrinking the window from the left and expanding it to the right by 1
        min_white = count_of_white
        for index in range(k,len(blocks)):
            if blocks[index-k]=='W':
                count_of_white-=1
            if blocks[index]=='W':
                count_of_white+=1
            min_white = min(min_white,count_of_white)
        return min_white
        #Time Complexity: O(n)
        #Space Complexity: O(1)