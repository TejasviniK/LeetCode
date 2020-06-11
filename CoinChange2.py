class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #amt_arr = [i for i in range(amount+1)]
        #coin_arr = [i f]
        col = amount + 1
        row = len(coins) + 1
        dp = [[0 for i in range(col)] for i in range(row)]
        print(dp)

        for i in range(1, col) :
            dp[0][i] = 0
        for i in range(row) :
            dp[i][0] = 1

        print(dp)
        for i in range(row) :
            for j in range(col) :
                if j >= coins[i-1] :
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[row-1][col-1]
        
s = Solution()
print(s.change(5,[1, 2, 5]))