class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        sayac = 0
        for num in batteryPercentages:
            if num - sayac > 0:
                sayac += 1
        return sayac