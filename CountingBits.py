class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0 :
            return [0]
        
        b_list = [0, 1]
        if num == 1 :
            return b_list
        
        #print(b_list)
        i = 0
        cur_num = 2
        num_range = cur_num * 2
        while len(b_list) < num+1 :
            if cur_num >= num_range :
                i = 0
                num_range = cur_num * 2
            b_list.append(1+b_list[i])
            cur_num += 1
            i += 1
        
        return b_list

    def countBitsApproach2(self, num):
        b_list = [0]
        for i in range(1,num+1) :
            b_list.append(b_list[int(i/2)] + i%2)
        return b_list

s = Solution()
print(s.countBits(16))
print(s.countBitsApproach2(16))