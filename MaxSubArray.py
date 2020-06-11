class Solution:
    def maxSubarraySumCircular(self, A) -> int:

        #print(A)

        kadane = self.kadane_max(A)
        if kadane < 0:
            return kadane
        wrap = 0
        for index in range(0, len(A)):
            wrap += A[index]
            A[index] = -A[index]
        #print("list after wrap :", A)
        #print("wrap :", wrap)
        wrap = wrap + self.kadane_max(A)

        if wrap > kadane :
            return wrap
        else :
            return kadane
        

        

    def kadane_max(self, A) -> int:
        list_max = cur_max = A[0]
        for i in range(1, len(A)) :
            cur_max = max(A[i], cur_max+A[i])
            if list_max < cur_max :
                list_max = cur_max
        return list_max


s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([3,-1,2,-1]))
print(s.maxSubarraySumCircular([3,-2,2,-3]))
print(s.maxSubarraySumCircular([-2,-3,-1]))