## 15. 3Sum
## https://leetcode.com/problems/3sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        doublets = []
        left = 0
        right = n-1
        while left<right:
            numsum = nums[left]+nums[right]
            if numsum>target:
                right-=1
            elif numsum<target:
                left+=1
            else:
                doublets.append([nums[left],nums[right]])
                left+=1
                right-=1
                while left<right:
                    if nums[left]==nums[left-1]:
                        left+=1
                    elif nums[right]==nums[right+1]:
                        right-=1
                    else:
                        break
        return doublets
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums = sorted(nums)
        triplets = []
        for i,a in enumerate(nums[:-2]):
            if i>0 and nums[i-1]==a:
                continue
            doublets = self.twoSum(nums[i+1:],-a)
            for doublet in doublets:
                b,c = doublet
                triplets.append([a,b,c])
        return triplets
    