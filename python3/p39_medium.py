## 39. Combination Sum
## https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates, target):
        comb = [(target,)] if target in candidates else []
        candidates = sorted([cand for cand in candidates if cand<target])
        comb.extend( [(cand,target-cand) for cand in candidates if (cand<=target-cand and target-cand in candidates)])
        remain = [(cand,target-cand) for cand in candidates if (cand<target-cand and target-cand>0)]
        while remain:
            newget = remain.pop()
            wand2 = newget[-2]
            for cand in candidates:
                wand1 = newget[-1]-cand
                if ( cand<=wand1 and cand>=wand2 and wand1 in candidates ):
                    comb.append(newget[:-1]+(cand,wand1))
                if cand<wand1 and cand>=wand2 and wand1>0:
                    remain.append(newget[:-1]+(cand,wand1))
        return comb

# import sys
# if __name__=='__main__':
#     candidatess = [[2,3,6,7],[2,3,5],[2],[1,2],[2,7,6,3,5,1]]
#     targets = [7,8,1,4,9]
#     chkout = [[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2],[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],[1,1,1,6],[1,1,2,2,3],[1,1,2,5],[1,1,7],[1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]
#     chkout = set(list(map(tuple,chkout)))
#     sol = Solution()
#     for candidates,target in zip(candidatess,targets):
#         print("Input: candidates =",candidates,", target =",target)
#         output = set(sol.combinationSum(candidates,target))
#         print("Output:", output)
#     print(output-chkout)
#     print(chkout-output)
