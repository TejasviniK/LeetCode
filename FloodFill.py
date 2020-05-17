
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int) :

        if 0 <= sr < len(image) and 0 <= sc < len(image[0]) :
            oldColor = image[sr][sc]
            if oldColor == newColor :
                return image
            image[sr][sc] = newColor
            if 0 <= sr+1 < len(image) and 0 <= sc < len(image[0]) and image[sr+1][sc] == oldColor:
                self.floodFill(image, sr+1, sc, newColor) #bottom
            if 0 <= sr-1 < len(image) and 0 <= sc < len(image[0]) and image[sr-1][sc] == oldColor:
                self.floodFill(image, sr-1, sc, newColor) #up
            if 0 <= sr < len(image) and 0 <= sc-1 < len(image[0]) and image[sr][sc-1] == oldColor:
                self.floodFill(image, sr, sc-1, newColor) #left
            if 0 <= sr < len(image) and 0 <= sc+1 < len(image[0]) and image[sr][sc+1] == oldColor:
                self.floodFill(image, sr, sc+1, newColor) #right

        return image

    def inImage(self, image, sr, sc) :
        return 0 <= sr < len(image) and 0 <= sc < len(image[0])
    
    def isOldClr(self, image, sr, sc, oldColor) :
        return image[sr][sc] == oldColor

s = Solution()
print(s.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))

