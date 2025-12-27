class Solution(object):
    def diStringMatch(self, s):
        a, match1,i_sayac, d_sayac = len(s), [],0,0
        for i in range(a):
            if s[i] == 'I':
                match1.append(i_sayac)
                i_sayac +=1
            if s[i] == 'D':      
                match1.append(a - d_sayac)
                d_sayac +=1
        match1.append(0)
        if s[a-1] == 'I':
            match1[a] = match1[a-1] + 1
        else:
            match1[a] = match1[a-1] - 1
        return match1