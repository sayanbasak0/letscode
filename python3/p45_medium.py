## 45. Jump Game II
## https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens<=1:
            return 0
        if lens==2:
            return 1
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(0, lens-1):
            farthest = max(farthest, i + nums[i])
            if farthest>=lens-1:
                return jumps+1
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps

    def jump2(self, nums: List[int]) -> int:
        if lens==2:
            return 1
        if lens==1:
            return 0
        steps_away = [0 for n in nums]
        j = lens-2
        steps_away[-1] = 0
        while j>=0:
            if j+nums[j]>=lens-1:
                steps_away[j] = 1
            elif nums[j]==0:
                steps_away[j] = lens
            else:
                steps_away[j] = min(steps_away[j+1:j+nums[j]+1])+1
            j-=1
        return steps_away[0]
                