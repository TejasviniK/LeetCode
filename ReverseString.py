class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j :
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

        return s
    
    def reverseString2(self, s, k):
        s_list = [i for i in s]
        def swap(left, right) :
            if left < right :
                s_list[left], s_list[right] = s_list[right], s_list[left]
                swap(left+1, right-1)
        
        for i in range(0, len(s), k*2) :
            if i+k-1 < len(s) :
                swap(i, i+k-1)

            else :
                swap(i, len(s)-1)

        return "".join(s_list)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        words = s.split()
        for w in words :
            r += w[::-1]
            r += " "
        return r

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """   
        def isVowel(ch) :
            return ch in "aeiou"

        s_list = [i for i in s]
        left = 0
        right = len(s)-1
        while left < right :
            while not isVowel(s_list[left]) :
                left += 1
            while not isVowel(s_list[right]) :
                right -= 1

            if left > right :
                break
            #print("left", left)
            #print("right", right)
            temp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = temp
            left += 1
            right -= 1
        
        return "".join(s_list)

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))
print(s.reverseString2("abcdefg", 2))
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseVowels("leetcode"))