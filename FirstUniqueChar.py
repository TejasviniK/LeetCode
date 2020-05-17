class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list = [ i for i in s ]

        if len(s) == 0 :
            return -1
        
        else :
            for i in range(len(s_list)):
                flag = False
                for j in range(len(s_list)):
                    if i != j and s_list[i] == s_list[j] :
                        flag = True
                        break
                    else :
                        continue
                if flag == True and i == len(s_list)-1 :
                    return -1
                elif flag == True :
                    continue
                else :
                    return i

s = Solution()
print(s.firstUniqChar("c"))