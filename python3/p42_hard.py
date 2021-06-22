## 42. Trapping Rain Water
## https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<3:
            return 0
        area = 0
        lmax = [0 for i in range(0,n)]
        rmax = [0 for i in range(0,n)]
        for i in range(1,n-1):
            lmax[i]=max(height[i-1],lmax[i-1])
            rmax[n-i-1]=max(height[n-i],rmax[n-i])
        for i in range(1,n-1):
            area += max(0,min(lmax[i]-height[i],rmax[i]-height[i]))
        return area
        