## 12. Integer to Roman
## https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        num_roman = [
            [1, 'I'],
            [5-1, 'IV'],
            [5, 'V'],
            [10-1, 'IX'],
            [10, 'X'],
            [50-10, 'XL'],
            [50, 'L'],
            [100-10, 'XC'],
            [100, 'C'],
            [500-100, 'CD'],
            [500, 'D'],
            [1000-100, 'CM'],
            [1000, 'M']
        ]
        romstr = ""
        for n,r in num_roman[::-1]:
            x = num//n
            romstr+=''.join([r]*x)
            num-=x*n
        return romstr