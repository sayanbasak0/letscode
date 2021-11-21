## 51. N-Queens
## https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        uncols = set([i for i in range (n)])
        undiags = set([i for i in range(-n+1,n)])
        unadiags = set([i for i in range(0,2*n-1)])
        
        configs = self.recurse(n, 0, uncols, undiags, unadiags)
        return configs
        
    def recurse(self, n, row, uncols, undiags, unadiags):
        # print(n, row, uncols, undiags, unadiags)
        configs = []
        if row==n:
            return configs
        for col in list(uncols):
            if ((row-col) in undiags) and ((row+col) in unadiags):
                
                config = [ ''.join('Q' if i==col else '.' for i in range(n)) ]
                if row==n-1:
                    configs.append(config)
                    print(n, row, uncols, undiags, unadiags)
                    print(config)
                else:
                    uncols.remove(col)
                    undiags.remove(row-col)
                    unadiags.remove(row+col)
                    configdepths = self.recurse(n, row+1, uncols, undiags, unadiags)
                    uncols.add(col)
                    undiags.add(row-col)
                    unadiags.add(row+col)
                    print(n, row, uncols, undiags, unadiags)
                    print(configdepths)
                    for configdepth in configdepths:
                        configs.append(config+configdepth)
                    
        return configs