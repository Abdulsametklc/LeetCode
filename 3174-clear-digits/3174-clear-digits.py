class Solution(object):
    def clearDigits(self, s):
        a = ""
        for st in s:
            if st.isdigit():
                if a:
                    a = a[:-1]
            else:
                a += st

        return a