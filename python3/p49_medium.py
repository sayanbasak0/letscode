## 49. Group Anagrams
## https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_str = {}
        for s in strs:
            s_count = ''.join(sorted(s))
            if tuple(s_count) in grp_str:
                grp_str[tuple(s_count)].append(s)
            else:
                grp_str[tuple(s_count)] = [s]
        return grp_str.values()
        
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        mapc = {chr(i+ord('a')):i for i in range(26)}
        grp_str = {}
        for s in strs:
            s_count = [0]*26
            for c in s:
                s_count[mapc[c]] += 1
            if tuple(s_count) in grp_str:
                grp_str[tuple(s_count)].append(s)
            else:
                grp_str[tuple(s_count)] = [s]
        return grp_str.values()