class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st1 = []
        for i in S:
            if i != '#':
                st1.append(i)
            else:
                if st1:
                    st1.pop()
        st2 = []
        for i in T:
            if i != '#':
                st2.append(i)
            else:
                if st2:
                    st2.pop()
        return st1 == st2
        