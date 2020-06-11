class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        A_len = len(A)+1
        B_len = len(B)+1
        
        dp = [[0 for i in range(B_len)] for i in range(A_len)]
        #print(dp)
        for i in range(1, A_len) :
            for j in range(1, B_len) :
                if A[i-1] == B[j-1] :
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                #print(dp[i][j], end="")
            #print("\n")

        return dp[A_len-1][B_len-1]
            



s = Solution()
#s.maxUncrossedLines([1,4,2], [1,2,4])
print(s.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
