from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        wdict = defaultdict(list)
        count  = 0
        
        for w in words:
            wdict[w[0]].append(w)
        
        for s in S:
            expecting_s = wdict[s]
            wdict[s] = []
            
            for word in expecting_s:
                if len(word) == 1:
                    count += 1
                else:
                    wdict[word[1]].append(word[1:])
        return count
