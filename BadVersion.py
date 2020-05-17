version = [False, False, False, True, True]
print(len(version))

def isBadVersion(v) :
    return version[v]

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n-1
        mid = int((end+start)/2)
        #print("Mid", mid)
        while(start < end) :
            print("Start", start)
            print("End", end)
            print("Mid", mid)
            flag = isBadVersion(mid)
            if(flag) :
                if mid == start :
                    return mid+1
                else :
                    end = mid
            else :
                start = mid + 1
            mid = int((end+start)/2)
        return end+1
s = Solution()
print(s.firstBadVersion(5))


