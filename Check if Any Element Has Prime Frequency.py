class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # count frequencies without using Counter
        for val in set(nums):              # loop unique elements
            if is_prime(nums.count(val)):  # check frequency directly
                return True
        return False
