class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a = [int(x) for x in boxes]
        indexes = []
        ans = []
        for i in range(len(a)):
            if a[i]==1:
                indexes.append(i)
        for i in range(len(a)):
            n = [abs(i-x) for x in indexes]
            ans.append(sum(n))
        return ans