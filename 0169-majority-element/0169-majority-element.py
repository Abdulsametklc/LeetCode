class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1 or len(set(nums))==1:
            return nums[0]
        s_nums = list(set(nums))
        uzunluk = len(nums)
        uzunluk_s = len(s_nums)
        sayac_list = []
        for i in range(uzunluk_s):
            sayac = 0
            for j in range(uzunluk):
                if s_nums[i] == nums[j]:
                    sayac +=1
            sayac_list.append(sayac)
        en_buyuk = sayac_list[0]
        indeks = 0
        for k in range(1,uzunluk_s):
            if en_buyuk < sayac_list [k]:
                en_buyuk = sayac_list[k]
                indeks = k
        return s_nums[indeks]