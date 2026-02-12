class Solution(object):
    def lemonadeChange(self, bills):
        para = {}
        para[5], para[10] = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                para[5] += 1
            elif bills[i] == 10:
                para[10] += 1
                if para[5] == 0:
                    return False
                else:
                    para[5] -= 1
            else:
                if para[5] == 0 or para[10] == 0:
                    if para[5] >= 3:
                        para[5] -= 3
                    else:
                        return False
                else:
                    para[5] -= 1 
                    para[10] -= 1
        return True