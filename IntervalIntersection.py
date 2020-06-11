class Solution(object):

    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        """

        aptr = 0
        bptr = 0
        a_len = len(A)
        b_len = len(B)
        res = []
        while aptr < a_len and bptr < b_len :
            #If intersection is present
            if A[aptr][0] <= B[bptr][1] and A[aptr][1] >= B[bptr][0] :
                temp = (max(A[aptr][0], B[bptr][0]), min(A[aptr][1], B[bptr][1]))
                res.append(temp)
            
            if A[aptr][1] < B[bptr][1] :
                aptr += 1
            else :
                bptr += 1
        
        return res

    def intervalIntersectionMyLogic(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        count = max(A[-1][1], B[-1][1])
        print(count)
        A_int = [0 for i in range(count+1)]
        B_int = [0 for i in range(count+1)]
        for i,j in A :
            for k in range(i, j+1) :
                A_int[k] = 1
        for i,j in B :
            for k in range(i, j+1) :
                B_int[k] = 1
        print(A_int)
        print(B_int)

        result = []
        index = 0
        in_progress = False
        for i,j in zip(A_int, B_int) :
            print(i,j)
            if i == 1 and j == 1 and i == j :
                print("Match 1")
                if in_progress :
                    index += 1
                    continue           
                else :
                    in_progress = True
                    start_idx = index
            else :
                if in_progress :
                    end_idx = index - 1
                    result.append([start_idx, end_idx])
                    in_progress = False
                else :
                    index += 1
                    continue
            index += 1
                    
            
        print(result)
        



s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

# 0 1, 1 2
# 1 2 2 5 5 8 10 12 13 15 23 24 24 25 25 26