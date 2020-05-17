import collections
class Solution:
    def singleNonDuplicate(self, nums) -> int:
        
        low = 0
        high = len(nums)-1
        #mid = int((low + high)/2)
        while low != high :
            mid = int((low + high)/2)
 
            if nums[mid] == nums[mid+1]  :
                if mid % 2 == 0:   #1,1,3,3,4,4,5,8,8
                    low = mid + 2
                else : #[3,3,7,10,10,11,11]
                    high = mid - 1

            elif nums[mid] == nums[mid-1] :
                if mid % 2 == 0: #[1,1,2,3,3,4,4,8,8]
                    high = mid - 2
                else : #[3,3,7,7,10,11,11]
                    low = mid + 1
            else :
                return nums[mid]
        
        return nums[low]
            

    def singleNonDuplicateMethod2(self, nums) :
        t = nums[0]
        print(t)

        for i in range(1, len(nums)):
            t ^= nums[i]
            print(t)

        return t

s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(s.singleNonDuplicate([3,3,7,7,10,11,11]))
print(s.singleNonDuplicate([1,1,3,3,4,4,5,8,8]))
print(s.singleNonDuplicate([3,3,7,10,10,11,11]))

print(s.singleNonDuplicateMethod2([3,3,7,10,10,11,11]))