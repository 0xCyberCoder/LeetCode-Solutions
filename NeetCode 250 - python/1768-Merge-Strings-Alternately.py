class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        rs = ""
        for i in range(len(word1) + len(word2)):
            if len(w1) != 0:
                rs += w1.pop(0)
            if len(w2) != 0:
                rs += w2.pop(0)
                
        return rs
    
