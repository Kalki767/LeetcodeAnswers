class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        extended_list =[] #creating empty list
        for start,end in ranges: #initalizing our list by extending it through it's start and end points
            extended_list.extend(list(range(start,end+1)))
        for i in range(left,right+1): #checking if each and every element exists in the extended list
            if i not in extended_list:
                return False
        return True
        