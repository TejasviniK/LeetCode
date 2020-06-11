class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        points.sort(key= lambda P : P[0]**2 + P[1]**2)

        return(points[:K])
        
s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))