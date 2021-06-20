## 27. Remove Element
## https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lenn = len(nums)
        if lenn<1:
            return lenn
        i,j = 0,0
        
        while j<lenn:
            if nums[j]!=val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i