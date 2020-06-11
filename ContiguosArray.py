from timeit import timeit
from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = defaultdict()
        global_max = 0
        sum = 0

        for i in range(len(nums)) :
            print("Loc -{}, value - {}".format(i,nums[i]))
            if nums[i] == 1 :
                sum += 1
            else :
                sum -= 1
            if sum == 0 :
                global_max = max(global_max, i + 1)
            if sum in hash :
                global_max = max(global_max, i - hash[sum])
            else :
                hash[sum] = i
            print(hash)
        
        return global_max

s = Solution()
print(s.findMaxLength([0,1,0]))

print(s.findMaxLength([1,1,0,0,1,1,0,1,1]))

