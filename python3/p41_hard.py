## 41. First Missing Positive
## https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums):
        lenum = len(nums)
        found1 = False
        for i in range(lenum):
            if not(found1) and nums[i]==1:
                found1 = True
                break
        if not found1:
            return 1
        for i in range(lenum):
            if nums[i]<=0 or nums[i]>lenum:
                nums[i] = 1
            
        for i in range(lenum):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        
        for i in range(lenum):
            if nums[i]>0:
                return i+1
        return lenum+1
        
    def firstMissingPositive2(self, nums):
        minset = set()
        lenum = len(nums)
        while nums:
            x = nums.pop()
            if x>0:
                minset.add(x)
        
        for i in range(1,lenum+2):
            if i not in minset:
                return i
        

import sys
if __name__=='__main__':
    numss = [[1,2,0],[3,4,-1,1],[7,8,9,11,12]]
    chkouts = [3,2,1]
    sol = Solution()
    for nums,chkout in zip(numss,chkouts):
        print("Input: nums =",nums)
        output = sol.firstMissingPositive2(nums)
        print("Output:", output)
        print(output==chkout)
        
