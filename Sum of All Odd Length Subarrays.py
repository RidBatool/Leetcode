class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total=0
        n= len(arr)
        for i in range(n):
            for j in range(i, n):
                length= j-i+1
                if length%2==1:
                    total+=sum(arr[i:j+1])
        return total  
