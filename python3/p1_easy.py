## 1. Two Sum
## https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numkeys = {}
       
        for i,num in enumerate(nums):
            if num in numkeys:
                return i, numkeys[num]
            else:   
                numkeys[target-num] = i
        