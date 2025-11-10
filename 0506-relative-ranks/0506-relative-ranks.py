class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        answer = [""] * n

        sirali = sorted(range(n), key=lambda i: score[i], reverse=True)

        for rank, i in enumerate(sirali):
            if rank == 0:
                answer[i] = "Gold Medal"
            elif rank == 1:
                answer[i] = "Silver Medal"
            elif rank == 2:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank + 1)
        
        return answer