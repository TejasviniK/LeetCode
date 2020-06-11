class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 :
            return False
        while n > 2 :
            rem = n % 2
            if rem :
                return False
            n = n / 2
        return True
    
s = Solution()
print(s.isPowerOfTwo(16))