class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i,steps=-1,0
        amount = capacity
        while i<len(plants)-1:
            if amount>=plants[i+1]:
                amount-=plants[i+1]
                steps+=1
                i+=1
            else:
                steps= steps+2*(i+1)
                amount = capacity
        return steps