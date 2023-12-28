class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maximum_number = len(arr)//4
        set_arr = {}
        for i in arr:
            if i in set_arr:
                set_arr[i]+=1
            else:
                set_arr[i]=1
        for key,value in set_arr.items():
            if value>maximum_number:
                return key
        return 0