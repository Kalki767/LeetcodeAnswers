class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = list(s)
        n = len(indices)
        for i in range(n):
            shuffled[indices[i]] = s[i]
        return "".join(shuffled)