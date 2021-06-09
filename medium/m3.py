class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        non_rep = ""
        max_len = 0
        for c in s:
            i = non_rep.find(c)
            if i<0:
                non_rep+=c
                max_len = max(len(non_rep),max_len)
            else:
                non_rep = non_rep[i+1:]+c
        
        return max_len
