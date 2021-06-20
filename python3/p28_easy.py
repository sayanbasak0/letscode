## 28. Implement strStr()
## https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needlen = len(needle)
        if needlen==0:
            return 0
        haylen = len(haystack)
        if haylen<needlen:
            return -1
        hi = 0
        while hi<haylen-needlen+1:
            nj = 0
            while nj<needlen and haystack[hi+nj] == needle[nj]:
                nj+=1
            if nj==needlen:
                return hi
            hi+=1
        return -1