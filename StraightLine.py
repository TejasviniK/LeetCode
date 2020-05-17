class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        #y = mx + c     
        print(coordinates)
        try :
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except :
            return False
        print(m)
        c = coordinates[0][1] - (m * coordinates[0][0]) 
        print(c)

        for x,y in coordinates :
            if y != m*x + c :
                print(x,y)
                return False
        
        return True




s = Solution()
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(s.checkStraightLine([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]))