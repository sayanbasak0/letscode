## 26. Remove Duplicates from Sorted Array
## https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenn = len(nums)
        if lenn<2:
            return lenn
        i,j = 0,1
        
        while j<lenn:
            if nums[i]!=nums[j]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1
        