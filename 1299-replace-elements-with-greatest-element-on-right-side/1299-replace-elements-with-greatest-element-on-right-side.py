class Solution(object):
    def replaceElements(self, arr):
        en_buyuk = -1

        for i in range(len(arr)-1,-1,-1):
            mevcut = arr[i]
            arr[i] = en_buyuk
            if mevcut > en_buyuk:
                en_buyuk = mevcut
        
        return arr