## 22. Generate Parentheses
## https://leetcode.com/problems/generate-parentheses/

from collections import deque
class Solution:
    parenth = {0:[],1:["()"]}
    def generateParenthesis(self, n):
        if n in Solution.parenth.keys():
            return Solution.parenth[n]
        parenth = set([])
        p1 = self.generateParenthesis(n-1)
        for p1i in p1:
            for i in range(len(p1i)+1):
                if i==len(p1i):
                    parenth.add("("+p1i+")")
                elif p1i[i]=='(':
                    parenth.add("("+p1i[:i]+")"+p1i[i:])
        Solution.parenth[n] = parenth
        return Solution.parenth[n]
    def generateParenthesis2(self, n):
        parenths = [["",0,0]]
        for i in range(2*n):
            parenthsLast = parenths
            parenths = []
            while parenthsLast:
                parenth,score,openBrace = parenthsLast.pop()
                if openBrace<n:
                    parenths.append([parenth+"(",score+1,openBrace+1])
                if score>0:
                    parenths.append([parenth+")",score-1,openBrace])
        return list(zip(*parenths))[0]
    def generateParenthesis3(self, n):
        parenths = deque([["",0,0]])
        while True:
            parenth,score,openBrace = parenths.popleft()
            if len(parenth)==2*n:
                parenths.append([parenth,score,openBrace])
                break
            if openBrace<n:
                parenths.append([parenth+"(",score+1,openBrace+1])
            if score>0:
                parenths.append([parenth+")",score-1,openBrace])
        return list(zip(*parenths))[0]
        
import sys
if __name__=='__main__':
    n = int(sys.argv[1])
    sol = Solution()
    print(len(sol.generateParenthesis3(n)))
    print(len(sol.generateParenthesis2(n)))
    print(len(sol.generateParenthesis(n)))
#     # print(sol.generateParenthesis(n))