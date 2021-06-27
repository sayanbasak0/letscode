## 47. Permutations II
## https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        numdict = {}
        for num in nums:
            numdict[num] = numdict.get(num,0)+1
        return self.subPermuteUnique(numdict)
    def subPermuteUnique(self,numdict):
        result = []
        for num,count in numdict.items():
            if count>0:
                numdict[num]-=1
                result = result+list(map(lambda x: [num]+x, self.subPermuteUnique(numdict)))
                numdict[num]+=1
        if result==[]:
            return [[]]
        return result

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        if(len(nums)==1):
            return [nums]
        else:
            exclude=set()
            result=[]
            for i in range(len(nums)):
                if(nums[i] not in exclude):
                    remPermutations=self.permuteUnique(nums[:i]+nums[i+1:])
                    for elem in remPermutations:
                        elem.append(nums[i])
                    exclude.add(nums[i])
                    result.extend(remPermutations)
            return result