class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = []
        #Get binary of number
        while(num > 0) :
            rem = num % 2
            num = int(num / 2)
            bin_num.append(rem)
        print("binary : ",bin_num.reverse())
        

        #Complement binary number
        comp = []
        for i in range(len(bin_num)) :
            if(bin_num[i]) :
                comp.append(0)
            else :
                comp.append(1)
        print("Complement : ", comp)
        
        #Decimal of complement
        dec_num = 0
        pow = 0
        for i in range(len(comp)-1, -1, -1) :
            dec_num += comp[i] * (2 ** pow)
            pow += 1

        print("Decimal :", dec_num)
        
        return dec_num

if __name__ == '__main__' :
    s = Solution()
    print(s.findComplement(1))

