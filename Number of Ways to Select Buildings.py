class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        ways=0
        one=zero=one_zero=zero_one=0
        for c in s:
            if c=='0':
                zero+=1
                one_zero+=one
                ways+=zero_one
            else:
                one+=1
                zero_one+=zero
                ways+=one_zero
        return ways
