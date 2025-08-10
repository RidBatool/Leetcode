from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count_n= Counter(str(n))
        for i in range(31):
            pow_n= Counter (str(1<<i))
            if count_n == pow_n:
                return True
        return False 
        
