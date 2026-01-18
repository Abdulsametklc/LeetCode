class Solution(object):
    def sumDivisibleByK(self, nums, k):
        repeat, toplam = {}, 0
        for n in nums:
            if n in repeat:
                repeat[n] += 1
            else:
                repeat[n] = 1
        
        for a,b in repeat.items():
            if b%k == 0:
                toplam += b*a
            
        return toplam       