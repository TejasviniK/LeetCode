class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_arr = []
        sum_arr.append(0)
        for i in range(1,len(nums)+1) :
            sum_arr.append(sum_arr[i-1] + nums[i-1])
        print(sum_arr)
        for i in range(len(nums)) :
            print(sum_arr[i])
            print(sum_arr[len(nums)]-sum_arr[i]-nums[i])
            if sum_arr[i] == (sum_arr[len(nums)]-sum_arr[i]-nums[i]) :
                print('Match!')
                return i
        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))