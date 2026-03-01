class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        max_time = releaseTimes[0]
        ans =  keysPressed[0]
        
        for i in range(1, len(keysPressed)):
            t = releaseTimes[i] - releaseTimes[i-1]
            
            if t > max_time or (t == max_time and keysPressed[i] > ans):
                max_time = t
                ans = keysPressed[i]
        
        return ans