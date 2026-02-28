class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        fark = 0
        for i in range(len(seats)):
            f = abs(seats[i] - students[i])
            fark += f
        return fark     