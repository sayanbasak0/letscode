## 14. Longest Common Prefix
## https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min([len(s) for s in strs])
        commonString = ""
        lenstrs = len(strs)
        for i in range(minlen):
            c = strs[0][i]
            j=1
            while j<lenstrs and c==strs[j][i]:
                j+=1
            if j==lenstrs:
                commonString += c
            else:
                break
        return commonString
    
