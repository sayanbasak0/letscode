## 34. Find First and Last Position of Element in Sorted Array
## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = [-1,-1]
        if len(nums)==0:
            return found
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return found
        if target<nums[0] or target>nums[len(nums)-1]:
            return found
        left = 0
        right = len(nums)-2
        if target==nums[0]:
            found[0] = 0
        else:
            while right>=left:
                index = (left+right)//2
                if nums[index]<target and nums[index+1]==target:
                        found[0] = index+1
                        left = index+1
                        break
                if nums[index]<target and nums[index+1]>target:
                    return found
                elif nums[index]>=target:
                    right = index-1
                else:
                    left = index+1
        right = len(nums)-2
        if target==nums[len(nums)-1]:
            found[-1] = len(nums)-1
        else:
            while right>=left:
                index = (left+right)//2
                if nums[index]==target and nums[index+1]>target:
                    found[-1] = index
                    break
                elif nums[index]>target:
                    right = index-1
                else:
                    left = index+1
        return found
        