class Solution(object):
    def romanToInt(self, s):
        roman_num = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }

        if 1<= len(s) <=15:
            prev_value=0
            index_sum=0
            for i in range(len(s)-1,-1,-1):
                value = roman_num[s[i]]
                if value < prev_value:
                    index_sum -= value
                else:
                    index_sum+=value
                
                prev_value = value
            return index_sum
        else: 
            return False        