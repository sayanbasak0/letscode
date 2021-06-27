## 50. Pow(x, n)
## https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            sgn = -1
            n = -n
        else:
            sgn = 1
        x_pow_n = 1
        while n>0:
            if n%2:
                x_pow_n *= x
            x *= x
            n //= 2
        if sgn<0:
            return 1/x_pow_n
        return x_pow_n