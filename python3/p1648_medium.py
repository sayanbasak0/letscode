## 1648. Sell Diminishing-Valued Colored Balls
## https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = sorted(inventory+[0],key=lambda x:-x)
        count = 0
        i = 1
        for od1,od2 in zip(inventory[:-1],inventory[1:]):
            if orders > i*(od1-od2):
                orders -= i*(od1-od2)
                count += i*(od1*(od1+1)-od2*(od2+1))//2
            else:
                od2_ = od1-orders//i
                orders -= i*(od1-od2_)
                count += i*(od1*(od1+1)-od2_*(od2_+1))//2
                # print(od1,od2,od2_,orders,i)
                count += orders*od2_
                orders = 0
                break
            i += 1
        return count%(10**9+7)