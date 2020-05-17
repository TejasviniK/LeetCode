from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust) -> int:
        judge_list = []
        people_list = []
        jp_dict = defaultdict(list)

        for p, j in trust :
            if not p in people_list :
                people_list.append(p)
            if not j in judge_list :
                judge_list.append(j)
            jp_dict[j].append(p)

        for j in jp_dict.keys() :
            print("j in dict", j)
            flag = True
            if j not in people_list :
                for i in range(1,N+1) :
                    if j == i :
                        continue
                    if i in jp_dict[j] :
                        continue
                    else :
                        flag = False
                        break
                if flag :
                    return j
                else :
                    continue
        return -1

    def findJudgeByCount(self, N: int, trust) -> int:
        count = [0] * (N + 1)
        print(count)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1   
            print(count)
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1   

s = Solution()
print(s.findJudgeByCount(2, [[1,2]]))