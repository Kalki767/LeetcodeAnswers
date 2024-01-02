class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for num in image: #traversing through the list
            i,j = 0,len(num)-1 
            while i<=j: #loop condition
                num[i],num[j]= abs(num[j]-1),abs(num[i]-1) #swapping elements
                i+=1
                j-=1
        return image