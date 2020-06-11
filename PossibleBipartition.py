class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        g1 = []
        g2 = []
        pos = 0
        while( pos < len(dislikes) ) :
            if (dislikes[pos][0] in g1 and dislikes[pos][1] in g1) or (dislikes[pos][0] in g2 and dislikes[pos][1] in g2) :
                return False

            if (dislikes[pos][0] not in g1 and dislikes[pos][1] not in g1) and (dislikes[pos][0] not in g2 and dislikes[pos][1] not in g2) :
                g1.append(dislikes[pos][0])
                g2.append(dislikes[pos][1])
            elif dislikes[pos][0] in g1 and dislikes[pos][1] not in g2 :
                g2.append(dislikes[pos][1])
            elif dislikes[pos][0] in g2 and dislikes[pos][1] not in g1 :
                g1.append(dislikes[pos][1])
            elif dislikes[pos][1] in g1 and dislikes[pos][0] not in g2 :
                g2.append(dislikes[pos][0])
            elif dislikes[pos][1] in g2 and dislikes[pos][0] not in g1:
                g1.append(dislikes[pos][0])
            # else :
            #     continue
                        
            pos += 1
        print("Grp1:", g1)
        print("Grp2:", g2)
        print("POS :", pos)
        
        # while pos < len(dislikes) :
        #     print(pos)
            
        #     if (dislikes[pos][0] in g1 and dislikes[pos][1] in g1) or (dislikes[pos][0] in g2 and dislikes[pos][1] in g2) :
        #         return False
        #     pos += 1
        return True



s = Solution()
#print(s.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
#print(s.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
#rint(s.possibleBipartition(3, [[1,2],[1,3],[2,4]]))
print(s.possibleBipartition(10,[[4,7],[4,8],[2,8],[8,9],[1,6],[5,8],[1,2],[6,7],[3,10],[8,10],[1,5],[7,10],[1,10],[3,5],[3,6],[1,4],[3,9],[2,3],[1,9],[7,9],[2,7],[6,8],[5,7],[3,4]]))