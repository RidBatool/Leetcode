class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_copy = str(num)
        max_ = num  # start with the original number
        for i in range(len(num_copy)):
            str1 = num_copy[:i]
            if num_copy[i] == '9':
                str1 += '6'
            elif num_copy[i] == '6':
                str1 += '9'
            str1 += num_copy[i+1:]
            if max_ < int(str1):
                max_ = int(str1)
        return max_
