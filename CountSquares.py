class Solution:
    def countSquares(self, matrix) -> int:
        count = 0
        m = len(matrix) #row
        n = len(matrix[0]) #column
        count_matrix = [[0 for i in range(n)] for i in range(m)]
        print(count_matrix)

        count_matrix[0] = matrix[0]
        for i in range(n) :
            count += count_matrix[0][i]

        for j in range(1,m) :
            count_matrix[j][0] = matrix[j][0]
            count += count_matrix[j][0]

        for i in range(1, m) :
            for j in range(1, n) : 
                if matrix[i][j] == 1 :
                    count_matrix[i][j] = min(count_matrix[i-1][j], count_matrix[i][j-1], count_matrix[i-1][j-1]) + 1
                    count += count_matrix[i][j]

        return count
        #print(count_matrix)

        

s = Solution()
s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])