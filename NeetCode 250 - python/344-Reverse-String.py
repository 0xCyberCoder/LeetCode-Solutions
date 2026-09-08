class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range (len(s)):
            y = len(s) - i - 1
            if i < y:
                a = s[i]
                b = s[y]
                
                s[i] = b
                s[y] = a
            else:
                break
