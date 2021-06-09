class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        maxPal = s[0:1]
        for i in range(1,2*len(s)-2):
            if i%2:
                j = 0
                while i//2-j>=0 and i//2+j+1<len(s) and s[i//2-j]==s[i//2+j+1]:
                    j+=1
                maxPal = maxPal if 2*j<=len(maxPal) else s[i//2-j+1:i//2+j+1]
                # print(maxPal,i,j)
            else:
                
                j = 0
                while i//2-j-1>=0 and i//2+j+1<len(s) and s[i//2-j-1]==s[i//2+j+1]:
                    j+=1
                maxPal = maxPal if 2*j+1<=len(maxPal) else s[i//2-j:i//2+j+1]
                # print(maxPal,i,j)
        return maxPal
           
