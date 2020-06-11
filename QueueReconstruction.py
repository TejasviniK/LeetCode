class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[]] * len(people)

        def findPlace(x) :
            high_num = 0
            for i in range(len(people)) :
                if len(res[i]) == 0 and high_num == x[1] :
                    return i
                elif len(res[i]) == 0 or res[i][0] >= x[0] :
                    high_num += 1
            
        people.sort(key= lambda x : x[0])

        for x in people :
            place = findPlace(x)
            res[place] = x
        
        return res

    def reconstructQueueApproach2(self, people):
        people.sort(key=lambda x:(-x[0],x[1]))
        print(people)

        res=[]
        
        for i in people:
            res.insert(i[1],i)
            
        return res

s = Solution()
#s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print(s.reconstructQueueApproach2([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))