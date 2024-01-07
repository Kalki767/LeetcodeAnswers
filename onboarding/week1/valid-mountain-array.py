class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3: #if the length of the array is less than 3 then return false
            return False
        i = 0
        while i<n-1: 
            if arr[i]==arr[i+1]: #if two elements are equal return False
                return False
            elif arr[i]>arr[i+1]: #when a bigger number is found break the loop
                break
            i+=1
        if i==n-1 or i==0: #if i is the start or the end of the array return False
            return False
        value = arr[i]
        i+=1
        while i<n:
            if value<arr[i]: #if elements that came after the value are less than it return False
                return False
            elif (i+1)<n and (arr[i]==arr[i+1] or arr[i]<arr[i+1]): #if the elements are not strictly decreasing
                return False
            i+=1
        return True