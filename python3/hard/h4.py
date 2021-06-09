## 4. Median of Two Sorted Arrays
## https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution: # O(log(min(m,n)))
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float: 
        
        len1 = len(nums1)
        len2 = len(nums2)
        if len1==0:
            if len2==0:
                return 1.0
            else:
                neg_inf = nums2[0]
                pos_inf = nums2[-1]
        else:
            if len2==0:
                neg_inf = nums1[0]
                pos_inf = nums1[-1]
            else:
                neg_inf = min(nums1[0],nums2[0])
                pos_inf = max(nums1[-1],nums2[-1])
        len1+=2
        len2+=2
        nums1 = [neg_inf]+nums1+[pos_inf]
        nums2 = [neg_inf]+nums2+[pos_inf]
        lent = len1+len2
        midpoint = (lent-1)//2
        median = 0
        if len1>len2:
            nums1,nums2 = nums2,nums1
            len1,len2 = len2,len1
        l1,r1 = 0,len1
        m1 = (l1+r1)//2
        m2 = midpoint - m1 - 1
        print(nums1,nums2)
        while True:
            print(m1,m2)
            if m1>=0 and m2+1<len2 and nums1[m1]>nums2[m2+1]:
                r1 = m1
                m1 = (l1+r1)//2
                m2 = midpoint - m1 -1
            elif m2>=0 and m1+1<len1 and nums1[m1+1]<nums2[m2]:
                l1 = m1
                m1 = (l1+r1)//2
                m2 = midpoint - m1 -1
            else:
                if lent%2:
                    return max(nums1[m1],nums2[m2])/1.0
                else:
                    return (max(nums1[m1],nums2[m2])+min(nums1[m1+1],nums2[m2+1]))/2.0
            
class Solution1: # O((m+n)log(m+n))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        numall = sorted(nums1+nums2)
        midpoints = (len(numall)-1)//2,(len(numall))//2
        return (numall[midpoints[0]]+numall[midpoints[1]])/2.0