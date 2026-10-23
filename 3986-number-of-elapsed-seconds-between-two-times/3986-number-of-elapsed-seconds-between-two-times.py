from datetime import datetime
class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        return int(abs((datetime.strptime(startTime,"%H:%M:%S") - datetime.strptime(endTime, "%H:%M:%S")).total_seconds()))