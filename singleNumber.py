import collections

class Solution:
    def singleNumber(self, nums) -> int:
        counter = collections.Counter(nums)

        for i in nums :
            if counter[i] == 1:
                return i
        

s = Solution()
print(s.singleNumber([4,1,2,1,2]))