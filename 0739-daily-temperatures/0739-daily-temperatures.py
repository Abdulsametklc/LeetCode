class Solution(object):
    def dailyTemperatures(self, temperatures): 
        a = [0] * len(temperatures)
        myStack = []

        for ix, temperature in enumerate(temperatures):
            while myStack and temperature > myStack[-1][0]:
                stackTemp, stackIndex = myStack.pop()
                a[stackIndex] = ix - stackIndex  
            myStack.append([temperature, ix])
        return a