class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
       count_columns = 0
       n = len(strs[0])
       for j in range(n): #iterate for each column in word
           i = 0
           while i<len(strs)-1:
               if ord(strs[i][j])>ord(strs[i+1][j]): #if they are not lexicographically sorted increment number of count
                   count_columns+=1
                   break
               else:
                    i+=1
       return  count_columns
        
             