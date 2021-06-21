## 35. Search Insert Position
## https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = -1
        if nums[0]>=target:
            return 0
        elif nums[len(nums)-1]<target:
            return len(nums)
        elif nums[len(nums)-1]==target:
            return len(nums)-1
        
        left = 0
        right = len(nums)-2
        while right>=left:
            index = (left+right)//2
            if nums[index]<target and nums[index+1]>=target:
                    return index+1
            elif nums[index]>=target:
                right = index-1
            else:
                left = index+1
        return found
        