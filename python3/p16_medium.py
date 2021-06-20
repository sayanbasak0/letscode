## 16. 3Sum Closest
## https://leetcode.com/problems/3sum-closest/

class Solution:
    def twoSumClosest(self, nums: List[int], num1: int, target: int, minsep: int, minsum: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        while left<right:
            numsum = nums[left]+nums[right]-target
            if numsum==0:
                return [numsum+target+num1,0]
            elif abs(numsum)<minsep:
                minsum = numsum+target+num1
                minsep = abs(numsum)
            if numsum>0:
                right-=1
            elif numsum<0:
                left+=1
        return [minsum,minsep]
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return []
        nums = sorted(nums)
        minsum = sum(nums[:3])
        minsep = abs(minsum-target)
        for i,a in enumerate(nums[:-2]):
            if i>0 and nums[i-1]==a:
                continue
            [minsum,minsep] = self.twoSumClosest(nums[i+1:], a, target-a, minsep, minsum)
            if minsep == 0:
                return minsum
        return minsum