## 32. Longest Valid Parentheses
## https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i,j = 0,len(s)-1
        while i<len(s) and s[i]==')':
            i+=1
        while j>=0 and s[j]=='(':
            j-=1
        if i<j:
            s = s[i:j+1]
        else: return 0
        
        dp = [0,0 if s[1]=='(' else 2]
        maxlen = dp[1]
        for i in range(2,len(s)):
            if s[i]=='(':
                dp.append(0)
            else:
                if s[i-1]=='(':
                    dp.append(dp[i-2]+2)
                    maxlen = max(dp[i],maxlen)
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp.append(dp[i-1]+2)
                    if i-dp[i-1]-2>=0:
                        dp[i]+=dp[i-dp[i-1]-2]
                    maxlen = max(dp[i],maxlen)
                else:
                    dp.append(0)
        return maxlen