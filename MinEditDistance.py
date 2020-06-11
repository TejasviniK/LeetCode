class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)+1
        n = len(word2)+1
        dp = [[0 for i in range(n) ] for j in range(m)]
        for i in range(m) :
            for j in range(n) :
                if i == 0 :
                    dp[i][j] = j
                elif j == 0 :
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1] :
                    dp[i][j] = dp[i-1][j-1]
                else :
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        print(dp)

        return dp[m-1][n-1]

s = Solution()
print(s.minDistance("abc", "bcd"))