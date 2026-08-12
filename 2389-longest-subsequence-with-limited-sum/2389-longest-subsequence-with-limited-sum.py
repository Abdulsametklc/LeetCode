class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        answer = []

        for q in queries:
            toplam = 0
            sayac = 0
            for num in nums:
                if toplam + num <= q:
                    toplam += num
                    sayac += 1
                else:
                    break
            answer.append(sayac)
        
        return answer