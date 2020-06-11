class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        max_idx = -1
        for idx,i in enumerate(nums) :
            if max_num < i :
                max_num = i
                max_idx = idx
        print(max_num)

        for i in nums :
            if i != max_num and i * 2 > max_num :
                print(i)
                return -1

        return max_idx
        
s = Solution()
print(s.dominantIndex([3, 6, 1, 0]))