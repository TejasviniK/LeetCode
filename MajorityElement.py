import collections
class Solution:
    def majorityElement(self, nums) -> int:

        counter = collections.Counter(nums)
        print(counter)

        for n in nums :
            if counter[n] > int(len(nums)/2) :
                return n

s = Solution()
print(s.majorityElement([3,2,3]))