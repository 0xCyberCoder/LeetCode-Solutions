class Solution:
    def validPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s) - 1
        while x < y:
            if s[x] == s[y]:
                x += 1
                y -= 1
            else:
                return self.validPalindrome2(s[x + 1:y + 1]) or self.validPalindrome2(s[x:y])
        return True
    def validPalindrome2(self, s: str) -> bool:
        x = 0
        y = len(s) - 1
        while x < y:
            if s[x] == s[y]:
                x += 1
                y -= 1
            else:
                return False
        return True
