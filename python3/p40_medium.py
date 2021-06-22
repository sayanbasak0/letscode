## 40. Combination Sum II
## https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates, target):
        coins = {}
        for cand in candidates:
            if cand<=target:
                coins[cand] = coins.get(cand,0)+1
        comb = [(target,)] if target in candidates else []
        remain = [({coin:1},target-coin,coin) for coin in coins if (target-coin>0)]
        coinsort = sorted(coins.keys())
        # print(coins)
        while remain:
            selcoins,newtarg,maxcoin = remain.pop()
            # print(selcoins,newtarg,maxcoin)
            for coin in coinsort:
                if maxcoin<=coin:
                    sel = selcoins.get(coin,0)
                    change = coins[coin]
                    left = newtarg-coin
                    if sel<change:
                        # print("Here")
                        if left>0:
                            selcoins[coin] = sel + 1
                            remain.append((selcoins.copy(),left,coin))
                            selcoins[coin] = sel
                        elif left==0:
                            selcoins[coin] = sel + 1
                            thiscomb = []
                            [thiscomb.extend([skey]*sval) for skey,sval in selcoins.items()]
                            thiscomb = tuple(thiscomb)
                            comb.append(thiscomb)
                            selcoins[coin] = sel

        return comb

# import sys
# if __name__=='__main__':
#     candidatess = [[10,1,2,7,6,1,5],[2,5,2,1,2],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#     targets = [8,5,27,27]
#     sol = Solution()
#     for candidates,target in zip(candidatess,targets):
#         print("Input: candidates =",candidates,", target =",target)
#         output = sol.combinationSum2(candidates,target)
#         print("Output:", output)
        
