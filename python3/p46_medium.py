## 46. Permutations
## https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        perm = []
        for i in range(len(nums)):
            perm = perm+list(map(lambda x:[nums[i]]+x,self.permute(nums[:i]+nums[i+1:])))
        return perm