## 10. Regular Expression Matching
## https://leetcode.com/problems/regular-expression-matching/

from collections import deque
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # stacksp = deque([[0,0]])
        stacksp = [[0,0]]
        plen = len(p)
        slen = len(s)
        donedict = {}
        while stacksp:
            si,pj = stacksp.pop()
            if str(si)+","+str(pj) in donedict.keys():
                continue
            else:
                donedict[str(si)+","+str(pj)] = 1
            
            if si==slen:
                if pj==plen:
                    return True
                if pj+1<plen and p[pj+1]=='*':
                    stacksp.append([si,pj+2])
            elif pj+1<plen and p[pj+1]=='*':
                stacksp.append([si,pj+2])
                if (p[pj]==s[si] or p[pj]=='.'):
                    stacksp.append([si+1,pj])
            elif pj<plen and (p[pj]==s[si] or p[pj]=='.'):
                stacksp.append([si+1,pj+1])
            # break
            # print(stacksp)
        return False

# import sys
# if __name__ == '__main__':
#     testcases = [
#         ["cat","c*cat"],
#         ["aa","a"],
#         ["aa","a*"],
#         ["ab",".*"],
#         ["aab","c*a*b"],
#         ["mississippi","mis*is*p*."],
#         ["mississippi","mis*is*ip*."],
#         ["abcd","d*"],
#         ["a","ab*"]
#     ]
#     # args,argp = sys.argv[1:]

#     solve = Solution()
#     for case,cape in testcases:
#         print([case,cape],solve.isMatch(case,cape))