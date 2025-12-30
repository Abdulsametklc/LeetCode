class Solution(object):
    def countStudents(self, students, sandwiches):
        one, zero = 0, 0
        for a in students:
            if a == 1:
                one += 1
            else:
                zero +=1
        
        for b in sandwiches:
            if b == 1:
                if one != 0:
                    one -= 1
                else:
                    return zero
            else:
                if zero != 0:
                    zero -= 1
                else:
                    return one            
        return 0