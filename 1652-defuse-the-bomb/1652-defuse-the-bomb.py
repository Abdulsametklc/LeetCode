class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n

        if k == 0:
            return result
        
        for i in range(n):
            toplam = 0

            if k > 0:
                for step in range(1, k+1):
                    toplam += code[(i + step)%n]
            
            else:
                for step in range(1, -k+1):
                    toplam += code[(i - step)%n]
            
            result[i] = toplam
        
        return result