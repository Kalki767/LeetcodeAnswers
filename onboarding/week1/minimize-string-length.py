class Solution:
    def minimizedStringLength(self, s: str) -> int:
        char_set = set(s)
        return len(char_set)