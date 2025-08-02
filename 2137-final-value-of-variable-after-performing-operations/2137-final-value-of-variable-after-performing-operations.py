class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                X +=1
            if operation == "--X" or operation == "X--":
                X -=1
        return X            