## 17. Letter Combinations of a Phone Number
## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    numDict = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'], 
        '7': ['p', 'q', 'r', 's'], 
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n<1:
            return []
        returnList = [""]
        for i,d in enumerate(digits):
            returnListTemp = returnList
            for j,l in enumerate(Solution.numDict[d]):
                if j==0:
                    returnList=list(map(lambda x: x+l, returnListTemp))
                else:
                    returnList+=list(map(lambda x: x+l, returnListTemp))

        # n = len(digits)
        # if n<1:
        #     return []
        # if n==1:
        #     return Solution.numDict[digits[0]]
        # listStrings = self.letterCombinations(digits[1:])
        # returnList = []
        # for l in Solution.numDict[digits[0]]:
        #     returnList+=list(map(lambda x: l+x, listStrings))
        # return returnList
        
        # for making dictionary
        # numDict = {}
        # leter = ord('a')
        # for i in range(2,10):
        #     if i==7 or i==9:
        #         numDict[str(i)] = [chr(leter),chr(leter+1),chr(leter+2),chr(leter+3)]
        #         leter+=4
        #     else:
        #         numDict[str(i)] = [chr(leter),chr(leter+1),chr(leter+2)]
        #         leter+=3
        # print(numDict)
        
