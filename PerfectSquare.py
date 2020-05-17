class Solution:
    # Not time efficient
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 :
            return True
        for i in range(2, int(num/2)+1) :
            print("i : ", i)
            if (num%i == 0) and (i ** 2 == num) :
                return True
        return False
    
    #Better than first
    def isPerfectSquareMethod2(self, num: int) -> bool:
        return ((int(num ** 0.5)) ** 2) == num

    #Too much better
    def isPerfectSquareMethod3(self, num: int) -> bool :
        if num < 2 :
            return True
        l = 2
        r = int(num / 2)
        
        while l <= r:
            mid = int((l + r) / 2)
            if mid ** 2 == num :
                return True
            elif mid ** 2 > num :
                r = mid - 1
            else :
                l = mid + 1

        return False


s = Solution()
#print(s.isPerfectSquare(9))
#print(s.isPerfectSquare(14))
print(s.isPerfectSquareMethod3(64))
#print(int(16 **))