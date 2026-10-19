class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if st:
                l = st[-1]
                if self.check_valid(s[i], l):
                    st.pop()
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        return not st

    def check_valid(self, x, y):
        if (x == ')' and y == '(') or (x == ']' and y == '[') or (x == '}' and y == '{'):
            return True
        return False