class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        costs.sort(key= lambda x: abs(x[0]-x[1]), reverse=True)
        print(costs)

        n = len(costs) / 2
        cost = 0
        a_cnt = 0
        b_cnt = 0
        for i in costs :
            print(i)
            if a_cnt == n :
                cost += i[1]
                b_cnt += 1
            elif b_cnt == n :
                cost += i[0]
                a_cnt += 1
            elif i[0] < i[1] :
                cost += i[0]
                a_cnt += 1
            else :
                cost += i[1]
                b_cnt += 1

        return cost

s = Solution()
print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))