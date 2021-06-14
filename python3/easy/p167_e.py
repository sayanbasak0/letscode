## 167. Two Sum II - Input array is sorted
## https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (left<right):
            sumn = numbers[left]+numbers[right]
            if sumn==target:
                return left+1,right+1
            elif sumn<target:
                left+=1
            else:
                right-=1