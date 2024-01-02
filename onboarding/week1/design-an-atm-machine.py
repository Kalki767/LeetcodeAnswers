class ATM:

        def __init__(self):
            self.money_in_ATM = {20:0,50:0,100:0,200:0,500:0} #to store money in the ATM
            self.money = [20,50,100,200,500] #storing banknotes in the ATM

        def deposit(self, banknotesCount: list[int]) -> None:
            for i in range(5): #inserting each banknotes with their correspondance key in the dictionary 
                index = self.money[i]
                self.money_in_ATM[index]+=banknotesCount[i]

        def withdraw(self, amount: int) -> list[int]:
            count_money = list(self.money_in_ATM.values()) #obtaining total money from our dictionary
            i=4
            ans =[0]*5
            while i>-1 and amount!=0:
                if amount>=self.money[i]: #checking if the amount is greater than the current banknote
                    index = self.money[i]
                    if count_money[i]>0: #checking if we have enough banknote
                        a = amount//index #calculating the number of banknotes we can use
                        minimum = min(a,count_money[i]) #taking the minimum between the calculated value and the amount we have
                        amount-=minimum*index #decremnting the amount by the minimum
                        ans[i]+=minimum
                        count_money[i]-=minimum
                    else:
                        i-=1
                else:
                    i-=1
            if amount==0: #if we succesfully represent our money with the given banknotes
                for i in range(5):
                    index = self.money[i]
                    self.money_in_ATM[index] -= ans[i]
                return ans
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)