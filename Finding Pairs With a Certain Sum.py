class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        
        # frequency map for nums2
        self.freq2 = {}
        for num in nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val

        # update freq2 for old value
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]

        # update freq2 for new value
        self.freq2[new_val] = self.freq2.get(new_val, 0) + 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        ans = 0
        for x in self.nums1:
            needed = tot - x
            if needed in self.freq2:
                ans += self.freq2[needed]
        return ans
