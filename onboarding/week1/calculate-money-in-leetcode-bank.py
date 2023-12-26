class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        start = 1
        div = n//7
        for i in range(div):
            total += 7/2 * (start * 2 + 6)
            start += 1
        remi = n % 7
        total += remi/2 * (start * 2  + remi - 1)
        return int(total)