## 7. Reverse Integer
## https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        resign = -1 if x<0 else 1
        reverxe = int(str(x)[::-1]) if x>=0 else -int(str(-x)[::-1])
        if reverxe<-2**31 or reverxe>2**31-1 :
            return 0
        return reverxe

class Solution1:
    def reverse(self, x: int) -> int:
        reverxe = 0
        resign = -1 if x<0 else 1
        x = x if x>=0 else -x
        while x>0:
            residue = x%10
            reverxe = reverxe*10+resign*residue
            if reverxe>2**31-1:
                return 0
            if reverxe<-2**31:
                return 0
            x = x//10
        return reverxe