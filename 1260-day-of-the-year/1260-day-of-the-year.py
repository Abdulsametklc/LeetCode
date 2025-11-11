class Solution(object):
    def dayOfYear(self, date):
        degerler = {
            "01":0,
            "02":31,
            "03":59,
            "04":90,
            "05":120,
            "06":151,
            "07":181,
            "08":212,
            "09":243,
            "10":273,
            "11":304,
            "12":334
        }
        
        yil = int(date[0:4])
        aranan = str(date[5]) + str(date[6])
        gun = int(str(date[8]) + str(date[9]))
        toplam = gun + degerler[aranan]

        if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
            if aranan > "02":  
                toplam += 1
        
        return toplam
        