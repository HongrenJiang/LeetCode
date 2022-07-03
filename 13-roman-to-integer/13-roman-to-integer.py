class Solution:
    def romanToInt(self, s: str) -> int:
        sysDict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, 
                   "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, 
                  "CM": 900, "M": 1000}
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in sysDict:
                num += sysDict[s[i:i+2]]
                i += 2
            else:
                num += sysDict[s[i]]
                i += 1
        return num