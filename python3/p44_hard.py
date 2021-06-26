## 44. Wildcard Matching
## https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        if plen==0:
            if slen==0:
                return True
            else:
                return False
        si = 0
        pi = 0
        pstar = -1
        sstar = -1
        while si<slen:
            if pi<plen and (p[pi]==s[si] or p[pi]=="?"):
                si += 1
                pi += 1
            elif pi<plen and (p[pi]=="*"):
                pstar = pi
                sstar = si
                pi += 1
            elif pstar==-1:
                return False
            else:
                pi = pstar+1
                si = sstar+1
                sstar += 1
        while pi<plen:
            if p[pi]!='*':
                return False
            pi+=1
        return True


    def isMatch2(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        if plen==0:
            if slen==0:
                return True
            else:
                return False
        psplit = p.split('**')
        while len(psplit)>1:
            p = '*'.join(psplit)
            psplit = p.split('**')
        print(p)
        # return True
        plen = len(p)
        stacksp = set([(0,0)])
        visited = set()
        while stacksp:
            si,pi = stacksp.pop()
            visited.add((si,pi))
            if si>=slen and pi>=plen:
                return True
            elif pi>=plen:
                pass
            elif si>=slen:
                if p[pi]=='*':
                    if (si,pi+1) not in visited:
                        stacksp.add((si,pi+1))
            elif p[pi]=='*':
                if (si+1,pi) not in visited:
                    stacksp.add((si+1,pi))
                if (si,pi+1) not in visited:
                    stacksp.add((si,pi+1))
            elif p[pi]=='?' or p[pi]==s[si]:
                if (si+1,pi+1) not in visited:
                    stacksp.add((si+1,pi+1))
                
        return False


# import sys
# if __name__=='__main__':
#     ss = ["aa","aa","cb","adceb","acdcb","mississippi"]
#     ps = ["a","*","?a","*a*b","a*c?b","m??*ss*?i*pi"]
#     chkouts = [False,True,False,True,False,False]
#     sol = Solution()
#     for s,p,chkout in zip(ss,ps,chkouts):
#         print("Input: s =",s,", p =",p)
#         output = sol.isMatch(s,p)
#         print("Output:", output,"(Check:",output==chkout,")")
        
