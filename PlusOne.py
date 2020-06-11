class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9 :
            digits[-1] = digits[-1]+1
            return digits

        num = 0
        for i in range(len(digits)-1, -1, -1) :
            num = (num * 10) + digits[i]

        print(num)
        new_num = num + 1
        num_str = str(new_num)
        new_num_list = []

        for i in num_str :
            new_num_list.append(i)

        return new_num_list



s = Solution()
print(s.plusOne([1, 2, 9]))