class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 1
        the_s = s[left:right+1]
        while right < len(s)-1:
            print(left,right,s[left], s[right])
            print(s[right+1])
            if s[right+1] in the_s:
                left = the_s.index(s[right+1]) + left
            right += 1
            the_s = s[left:right+1]
            max_len = len(the_s) if len(the_s) > max_len else max_len
            print('*', the_s, max_len)

        return max_len




s = 'pwwkew'
# s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))