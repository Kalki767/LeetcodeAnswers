class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1, number2=0,0
        for i in num1:
            number1=number1*10+(ord(i)-48)
        for i in num2:
            number2=number2*10+(ord(i)-48)
        product = number1*number2
        return str(product)