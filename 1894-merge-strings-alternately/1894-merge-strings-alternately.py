class Solution(object):
    def mergeAlternately(self, word1, word2):
        a,b = len(word1), len(word2)
        c= min(a,b)
        liste = [""] * (a+b)

        for i in range(c):
            liste[2*i] = word1[i]
            liste[2*i+1] = word2[i]

        if a<b:
            for k in range(2*c,c+b):
                liste[k]=word2[k-c]

        elif a>b:
            for k in range(2*c,c+a):
                liste[k]=word1[k-c]

        return "".join(liste)