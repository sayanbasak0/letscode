## 30. Substring with Concatenation of All Words
## https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        lenwords = len(words)
        wordslen = wordlen*lenwords
        slen = len(s)
        if slen<wordslen:
            return []
        si=0
        wordict = defaultdict(int)
        for word in words:
            wordict[word] = wordict[word] + 1
        ret = []
        while si<slen-wordslen+1:
            wdict = defaultdict(int)
            # print(wdict)
            sij = si
            total=0
            while total<lenwords and wordict[s[sij:sij+wordlen]] > 0:
                wdict[s[sij:sij+wordlen]] += 1
                if wdict[s[sij:sij+wordlen]] > wordict[s[sij:sij+wordlen]]:
                    break
                sij += wordlen
                total+=1
            if total==lenwords:
                ret.append(si)
            si+=1
        return ret

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        lenwords = len(words)
        wordslen = wordlen*lenwords
        slen = len(s)
        if slen<wordslen:
            return []
        wordict = {}
        for word in words:
            wordict[word] = wordict.get(word,0) + 1
        ret = []
        for wstart in range(wordlen):
            wstarthere = wstart
            total = 0
            wdict = {}
            for sstart in range(wstart,slen,wordlen):
                neword = s[sstart:sstart+wordlen]
                if neword in words:
                    wdict[neword] = wdict.get(neword,0) + 1
                    total += 1
                    while wdict[neword]>wordict[neword]:
                        wdict[s[wstarthere:wstarthere+wordlen]] -= 1
                        wstarthere += wordlen
                        total-=1
                    if total==lenwords:
                        ret.append(wstarthere)
                else:
                    wstarthere = sstart+wordlen
                    total = 0
                    wdict = {}
                    
        return ret