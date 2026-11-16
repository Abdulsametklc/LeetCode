class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            yeni_s = ""

            for i in range(0, len(s), k):
                grup = s[i:i+k]

                toplam = 0
                for a in grup:
                    toplam += int(a)

                yeni_s += str(toplam)
            
            s= yeni_s
        
        return s