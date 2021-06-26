## 43. Multiply Strings
## https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0"or num2=="0":
            return "0"
        numout = [0]
        for i1,n1 in enumerate(num1[::-1]):
            for i2,n2 in enumerate(num2[::-1]):
                nout = (int(n1)*int(n2))
                carry = 0
                it = 0
                while carry!=0 or nout>0:
                    if nout>0:
                        nt = nout%10
                        nout = nout//10
                    else: nt = 0
                    index = i1+i2+it
                    while index>len(numout)-1:
                        numout.append(0)
                    nadd = nt+numout[index]+carry
                    numout[index] = nadd%10
                    carry = nadd//10
                    it+=1
        return ''.join(map(str,numout[::-1]))

    def multiply2(self, num1: str, num2: str) -> str:
        if num1=="0"or num2=="0":
            return "0"
        numout = ["0"]
        for i1,n1 in enumerate(num1[::-1]):
            for i2,n2 in enumerate(num2[::-1]):
                nout = str(int(n1)*int(n2))
                carry = 0
                it = 0
                while carry!=0 or it<len(nout):
                    if it<len(nout):
                        nt = nout[len(nout)-1-it]
                    else: nt = "0"
                    index = i1+i2+it
                    while index>len(numout)-1:
                        numout.append("0")
                    nadd = str(int(nt)+int(numout[index])+carry)
                    numout[index] = nadd[-1]
                    if len(nadd)>1:
                        carry = int(nadd[0])
                    else:
                        carry = 0
                    it+=1
        return ''.join(numout[::-1])


# import sys
# if __name__=='__main__':
#     num1s = ["120","341","6"]
#     num2s = ["789","112","501"]
#     sol = Solution()
#     for num1,num2 in zip(num1s,num2s):
#         print("Input: num1 =",num1,", num2 =",num2)
#         output = sol.multiply(num1,num2)
#         print("Output:", output,"(Check:",int(num1)*int(num2),")")
#         print(int(output)==(int(num1)*int(num2)))
        
