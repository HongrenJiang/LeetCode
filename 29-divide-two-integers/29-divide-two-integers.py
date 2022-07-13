class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = -dividend
        if divisor < 0:
            negatives += 1
            divisor = -divisor
        
        res = 0
        while dividend - divisor >= 0:
            tem = divisor
            mul = 1
            while dividend - tem >= 0:
                res += mul
                dividend -= tem
                mul += mul
                tem += tem
        
        if negatives == 1:
            res = -res
        
        if res < -2 ** 31:
            res = -2 ** 31
            
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        
        return res
