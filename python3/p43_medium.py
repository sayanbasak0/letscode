## 43. Multiply Strings
## https://leetcode.com/problems/multiply-strings/

#################
#### TESTING ####
#################
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0"or num2=="0":
            return "0"
        numout = "0"
        for i1,n1 in enumerate(num1):
            for i2,n2 in enumerate(num2):
                nout = str(int(n1)*int(n2))
                carry = 
                for it,nt in enumerate(nout):
                    index = len(numout)-1-i1-i2-it
                    nadd = int(nt)+int(numout[index])+carry