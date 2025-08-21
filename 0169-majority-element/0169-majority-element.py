class Solution(object):
    def majorityElement(self, nums):
        nums_u= list(dict.fromkeys(nums))
        uzunluk = len(nums)
        uzunluk_u = len(nums_u)
        max_sayac = 0
        a=None

        for i in range(uzunluk_u):
            sayac = 0
            for j in range(uzunluk):
                if nums_u[i] == nums[j]:
                    sayac +=1

            if sayac > max_sayac:
                max_sayac = sayac
                a = nums_u[i]

        return a                        