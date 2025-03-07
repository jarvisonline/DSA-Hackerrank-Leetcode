class Solution:
    def _sieve(self, upper_limit):
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False 

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left, right):
        sieve_array = self._sieve(right)

        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]

        if len(prime_numbers) < 2:
            return -1, -1  

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair