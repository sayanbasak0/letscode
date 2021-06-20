## 20. Valid Parentheses
## https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        parrenth = "0"
        cmap = {"0":"","(":")", "{":"}","[":"]"}
        for c in s:
            # print(parrenth)
            if c  in ["(","{","["]:
                parrenth+=c
            elif cmap[parrenth[-1]]==c:
                parrenth = parrenth[:-1]
            else:
                return False
        if parrenth=="0":
            return True
        else:
            return False