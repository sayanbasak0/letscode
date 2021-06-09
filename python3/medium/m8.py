## 8. String to Integer (atoi)
## https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # print(s)
        s = s.strip()
        if len(s)==0:
            return 0
        mult = -1 if s[0]=='-' else 1
        s = s[1:] if s[0] in ['-','+'] else s
        number = 0
        if len(s)==0:
            return 0
        while s[0].isdigit():
            number = number*10+mult*int(s[0])
            if number<=-(2**31):
                return -(2**31)
            if number>(2*(2**30-1)):
                return (2**31-1)
            if len(s)>1:
                s = s[1:]
            else:
                break
                
        return number