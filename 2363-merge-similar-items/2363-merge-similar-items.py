class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        ret = []

        for i in range(len(items1)):
            for j in range(len(items2)):
                if items1[i][0] == items2[j][0]:
                    items1[i][1] += items2[j][1]
                    break

            ret.append(items1[i])

        for j in range(len(items2)):
            if items2[j][0] not in [x[0] for x in items1]:
                ret.append(items2[j])

        ret.sort()

        return ret