class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        n = len(s)
        number = 0
        while i < n:
            first, second = 0, 0
            if s[i] in roman_dict:
                first = roman_dict[s[i]]
            if i + 1 < n and s[i + 1] in roman_dict:
                second = roman_dict[s[i + 1]]

            if first < second:
                number += (second - first)
                i += 2
            else:
                number += first
                i += 1

        return number

