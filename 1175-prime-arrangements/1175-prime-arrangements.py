class Solution(object):
    def numPrimeArrangements(self, n):
        MOD = 10**9 + 7
        count = 0
        for num in range(2, n+1):
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                count += 1
        fact_prime = 1
        for i in range(1, count+1):
            fact_prime = (fact_prime * i) % MOD

        fact_non_prime = 1
        for i in range(1, n-count+1):
            fact_non_prime = (fact_non_prime * i) % MOD

        return (fact_prime * fact_non_prime) % MOD