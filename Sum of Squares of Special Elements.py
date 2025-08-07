class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        counter=1
        value=0
        for i in range(len(nums)):
            if n%counter==0:
                square= nums[i]**2
                value+=square
            counter+=1
        return value
