class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        t = 0
        command = {
            "RIGHT": 1,
            "LEFT" : -1,
            "DOWN" : n,
            "UP" : -n
        }
        for s in commands:
            t += command[s]
        return t    