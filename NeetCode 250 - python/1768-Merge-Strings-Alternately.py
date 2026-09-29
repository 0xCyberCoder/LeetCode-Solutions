class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        rs = ""
        while len(w1) > 0 or len(w2) > 0:
            if len(w1) != 0:
                rs += w1.pop(0)
            if len(w2) != 0:
                rs += w2.pop(0)
                
        return rs
    
