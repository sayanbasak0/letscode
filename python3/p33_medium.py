## 33. Search in Rotated Sorted Array
## https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l-1
        if l==1:
            if target==nums[0]:
                return 0
            else: return -1
        elif nums[0]<nums[-1]:
            if target<nums[0] or target>nums[l-1]:
                return -1
            pivot = 0
        else:
            if target<nums[0] and target>nums[l-1]:
                return -1
            while right>left:
                index = (left+right)//2
                if nums[index]>nums[index+1]:
                    break
                elif nums[index]<nums[0]:
                    right = index
                else:
                    left = index
            if target>=nums[0]:
                left = 0
                right = index
            else: # if target<=nums[l-1]:
                left = index+1
                right = l-1
            
        
        while right>=left:
            index = (left+right)//2
            if nums[index]==target:
                return index
            elif nums[index]>target:
                right = index-1
            else:
                left = index+1
        return -1