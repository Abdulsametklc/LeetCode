class Solution(object):
    def distributeCandies(self, candyType):
        if len(list(set(candyType))) > len(candyType)/2:
            return len(candyType)/2
        
        else:
            return len(list(set(candyType)))

        