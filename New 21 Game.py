class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)   # dp[i] = probability of getting exactly i points
        dp[0] = 1.0            # start with 0 points, probability = 1
        window_sum = 1.0       # sliding window sum of last maxPts dp values
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts  # average probability from last maxPts states

            if i < k:
                window_sum += dp[i]      # still drawing → include in window
            else:
                result += dp[i]          # stopped drawing → final score

            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]  # maintain sliding window

        return result
