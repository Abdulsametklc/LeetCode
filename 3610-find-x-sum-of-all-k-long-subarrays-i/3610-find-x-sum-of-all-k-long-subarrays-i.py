class Solution(object):
    def findXSum(self, nums, k, x):
        answer = []
        for i in range(len(nums) - k + 1):
            sira = {}
            sub = nums[i : i + k]
            for num in sub:
                if num not in sira:
                    sira[num] = 1
                else:
                    sira[num] += 1

            sirali = sorted(sira.items(), key=lambda t: (-t[1], -t[0]))
            secimler = sirali[:x]
            secilen_sayilar = set([t[0] for t in secimler])
            toplam = 0
            for ele in sub:
                if ele in secilen_sayilar:
                    toplam += ele
            answer.append(toplam)
        return answer