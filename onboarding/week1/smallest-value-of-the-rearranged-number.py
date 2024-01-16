class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        count_of_zero = 0
        ans = abs(num)
        nums =[]
        while ans>0:
            if ans%10!=0:
                nums.append(ans%10)
            else:
                count_of_zero+=1
            ans//=10
        ans =0
        n =len(nums)
        if num>0:
            nums.sort()
            ans = nums[0]
            index =1
            for i in range(count_of_zero):
                ans*=10
            while index<n:
                ans = ans*10+nums[index]
                index+=1
        else:
            index = 0
            nums.sort(reverse=True)
            while index<n:
                ans = ans*10+nums[index]
                index+=1
            for i in range(count_of_zero):
                ans*=10
            ans*=-1
        return ans
            