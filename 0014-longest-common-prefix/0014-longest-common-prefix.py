class Solution(object):
    def longestCommonPrefix(self, strs):
        output = ""
        for a in range(0,200):
            try:
                first = strs[0][a]
            except IndexError:
                return output

            for i in range(0,len(strs)):
                try:
                    second = strs[i][a]
                except IndexError:
                    return output

                if first != second:
                    return output
            output += first
        return output