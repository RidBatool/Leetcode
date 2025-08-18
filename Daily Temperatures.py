class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []  # will store indices
        
        for i, temp in enumerate(temperatures):
            # while current temp is greater than the temp at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx  # days until warmer temp
            stack.append(i)  # add current index to stack
        
        return ans
