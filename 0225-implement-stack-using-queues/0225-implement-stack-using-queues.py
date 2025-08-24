class MyStack(object):

    def __init__(self):
        self.MyQueue = deque()

    def push(self, x):
        self.MyQueue.append(x)

    def pop(self):
        for i in range(len(self.MyQueue)-1):
            self.MyQueue.append(self.MyQueue.popleft())
        return self.MyQueue.popleft()

    def top(self):
        return self.MyQueue[-1]

    def empty(self):
        return len(self.MyQueue) == 0