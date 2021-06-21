## 31. Next Permutation
## https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        loci = -1
        for i in range(lenn-1,0,-1):
            if nums[i]>nums[i-1]:
                loci = i-1
                locj = i
                for j in range(i,lenn):
                    if nums[loci]<nums[j]:
                        locj = j
                    else: break
                nums[loci],nums[locj] = nums[locj],nums[loci]
                nums[loci+1:] = nums[lenn-1:loci:-1]
                break
        if loci==-1:
            nums[:] = nums[::-1]