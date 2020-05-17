class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k :
            return "0"
        rem_num = num[:(len(num)-k)]
        print(rem_num)
        j = k        
        rem_num_list = [ i for i in rem_num]

        zero_string = []

        while k > 0 :
            if '0' in rem_num_list :
                loc = rem_num_list.index('0')
                print("loc of 0 ", loc)
                
                max_num = max(rem_num_list[0:loc])
                rem_num_list.remove(max_num)
                print("Removed :", max_num)
                k -= 1

                print("rem_num_list_till 0", rem_num_list[0:loc])
                loc = rem_num_list.index('0')
                if not rem_num_list[0:loc] :
                    zero_string.append("0")
                    print("zero string appended 0:", zero_string)
                    rem_num_list.remove("0")
                    print("rem_num_list_till_0 after 0 removal", rem_num_list[0:loc])
            
            else :
                if not rem_num_list :
                    print("K is not 0 but list is empty")
                    zero_string.remove("0")

                else :
                    max_num = max(rem_num_list)
                    rem_num_list.remove(max_num)

                k -= 1
            
            print("rem_num_list :", rem_num_list)

        print("zero_string before extend: ", zero_string)
        print("rem_num_list before extend :", rem_num_list)

        zero_string.extend(rem_num_list)
        zero_string.extend([ i for i in num[-j:]])

        print("zero_string : ", zero_string)
        print("last digits : ", num[-j:])
        final_str = ""
        for i in zero_string :
            final_str += i

        print(final_str)

        return int(final_str)

    def removeKdigitsStackMethod(self, num: str, k: int) -> str:

        stack = []

        for i in num :
            while k > 0 and len(stack) > 0 and stack[-1] > i :
                stack.pop()
                k -= 1
            stack.append(i)

        while k!= 0 and len(stack) > 0 :
            stack.pop()

        if len(stack) > 0 :
            return str(int(("".join(stack))))
        return "0"

s = Solution()
print(s.removeKdigitsStackMethod("102000",2))
print(s.removeKdigitsStackMethod("1320567",2))

