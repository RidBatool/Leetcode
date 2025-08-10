class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr_=[]
        nums_copy= nums[:]
        nums_copy.sort()
        while nums_copy:
            a= nums_copy.pop(0)
            b= nums_copy.pop(0)
            arr_.append(b)
            arr_.append(a)
        return arr_
