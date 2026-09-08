class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range (len(s)):
            y = len(s) - i - 1
            if i < y:
                temp = s[i]                
                s[i] = s[y]
                s[y] = temp
            else:
                break
