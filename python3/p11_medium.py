## 11. Container With Most Water
## https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height)<=1:
            return 0
        areaMax = 0
        start = 0
        end = len(height)-1
        while start<end:
            areaMax = max(areaMax,min(height[start],height[end])*(end-start))
            if height[start]>height[end]:
                end-=1
            else: start+=1
            # elif height[start]<height[end]:
            #     start+=1
            # else:
            #     if height[start+1]>height[end-1]:
            #         start+=1
            #     else:
            #         end-=1
        return areaMax