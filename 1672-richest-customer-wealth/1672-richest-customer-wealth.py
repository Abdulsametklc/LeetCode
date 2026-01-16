class Solution(object):
    def maximumWealth(self, accounts):
        a,b = len(accounts[0]),0
        for i in range(len(accounts)):
            toplam = 0
            for k in range(a):
                toplam += accounts[i][k]
            
            if toplam > b:
                b = toplam
        return b   