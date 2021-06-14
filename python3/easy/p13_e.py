## 
## 

class Solution:
    def romanToInt(self, s: str) -> int:
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
        num = 0
        for n,r in num_roman[::-1]:
            while len(s)>0 and s[0:len(r)]==r:
                num+=n
                if len(r)>=len(s):
                    s = ""
                else:
                    s = s[len(r):]
        return num