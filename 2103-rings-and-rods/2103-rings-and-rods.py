class Solution(object):
    def countPoints(self, rings):
        count= 0
        control = [[False, False, False] for _ in range(10)]

        for i in range(0,len(rings),+2):
            if rings[i] == "R":
                control[int(rings[i+1])][0] = True
            
            elif rings[i] == "G":
                control[int(rings[i+1])][1] = True

            elif rings[i] == "B":
                control[int(rings[i+1])][2] = True
        
        for i in range(len(control)):
            if control[i][0] and control[i][1] and control[i][2]:
                count += 1
        
        return count