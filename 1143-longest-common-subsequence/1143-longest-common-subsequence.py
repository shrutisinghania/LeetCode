class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(t1, t2, l1, l2, dp):
            if l1 == 0 or l2 == 0:
                return 0
            if dp[l1][l2] != -1:
                return dp[l1][l2]
            if t1[l1 - 1] == t2[l2 - 1]:
                dp[l1][l2] = 1 + lcs(t1, t2, l1-1, l2 -1, dp)
                return dp[l1][l2]
            dp[l1][l2] = max(lcs(t1, t2, l1 - 1, l2, dp), lcs(t1, t2, l1, l2 - 1, dp))
            return dp[l1][l2]
        
        dp = [[-1 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        return lcs(text1, text2, len(text1), len(text2), dp)