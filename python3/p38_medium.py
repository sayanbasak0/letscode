## 38. Count and Say
## https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        cay = "1"
        while n>1:
            i=0
            ci = cay[0]
            cayan = ""
            for c in cay:
                if ci==c:
                    i+=1
                else:
                    cayan+=f"{i}{ci}"
                    i=1
                    ci=c
            cayan+=f"{i}{ci}"
            cay = cayan
            n-=1
        return cay