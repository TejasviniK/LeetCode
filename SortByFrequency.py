import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = [i for i in s]
        counter = collections.Counter(s_list)
        sorted_dict = sorted(counter.items(), key= lambda kv : kv[1], reverse=True)
        #print(sorted_dict)

        return "".join([k*v for k,v in sorted_dict] )
        # for k,v in sorted_dict :
        #     print(k*v)

s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("Aabb"))