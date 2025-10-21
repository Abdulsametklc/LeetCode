class Solution(object):
    def getRow(self, rowIndex):
        curr_row = [1]
        for i in range(rowIndex):
            prev_row = curr_row
            curr_row = [1]
            for j in range(1, len(prev_row)):
                curr_row.append(prev_row[j-1]+prev_row[j])
            curr_row.append(1)
        return curr_row