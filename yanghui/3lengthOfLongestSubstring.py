class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            the_str = s[left:right+1]
            max_len = len(the_str) if max_len < len(the_str) else max_len
            if right + 1 == len(s):
                break
            if s[right+1] in the_str:
                left = the_str.index(s[right+1]) + left + 1
            right +=1
        return max_len

solution= Solution()
a = 'abcabcesac'
print(solution.lengthOfLongestSubstring(a))

