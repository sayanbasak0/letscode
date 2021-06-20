## 29. Divide Two Integers
## https://leetcode.com/problems/divide-two-integers/

class Solution:
    maxInt = 2**31-1
    minInt = -2**31
    maxInt2 = 2**30
    minInt2 = -2**30
    def divide(self, dividend: int, divisor: int) -> int:
        q = 1 
        sigbit = 1 if ((dividend>=0 and divisor>=0) or (dividend<0 and divisor<0)) else -1
        dividend = dividend if dividend>=0 else -dividend
        divisor = divisor if divisor>=0 else -divisor
        quotient = 0
        while dividend - divisor>0:
            if q==Solution.maxInt2:
                break
            q += q
            divisor += divisor
        while q>=1:
            if dividend-divisor>=0:
                quotient += q
                dividend -= divisor
            q = q>>1
            divisor = divisor>>1
        if sigbit>0:
            return quotient
        else:
            if quotient==Solution.maxInt and dividend>0:
                return Solution.minInt
            else:
                return -quotient
            