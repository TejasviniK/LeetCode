class Solution:
    def isHappy(self, n: int) -> bool:
        
        num_list = []

        while n != 1 :
            num_list.append(n)
            sum = 0
            while n > 0 :
                rem = n % 10  #9
                sum = sum + (rem ** 2) 
                n = int(n / 10) #1
            print("sum : ", sum)
            if sum not in num_list :
                n = sum
            else :
                return False
                
        return True

    def isHappyRec(self, n: int) -> bool:
        
        sum = 0
        while n > 0 :
            rem = n % 10  #9
            sum = sum + (rem ** 2) 
            n = int(n / 10) #1
        print("sum : ", sum)

        if sum < 10 :
            return sum == 1 or sum == 7
        
        return self.isHappyRec(sum)
 
s = Solution()
print(s.isHappyRec(7))


