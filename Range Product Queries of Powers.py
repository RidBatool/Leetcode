class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # build list of exponents for set bits of n (in non-decreasing order)
        exps = []
        i = 0
        while (1 << i) <= n:
            if (n >> i) & 1:
                exps.append(i)   # store exponent i (value = 2**i)
            i += 1

        # prefix sums of exponents: pref[k] = sum of exps[:k]
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        ans = []
        for left, right in queries:
            total_exp = pref[right + 1] - pref[left]
            ans.append(pow(2, total_exp, MOD))
        return ans
