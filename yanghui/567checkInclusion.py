class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        flag = False
        the_s_left = s1
        while left < len(s2):
            if s2[left] not in s1:
                left = left + 1
                the_s_left = s1
                print(left)
            elif s2[left] not in the_s_left:
                
            else:
                the_s_left = the_s_left.replace(s2[left], '', 1)
                left = left + 1
            if the_s_left == '':
                flag = True
                break
        return flag


solution = Solution()
a = 'abcabcesac'
b = 'ccba'
print(solution.checkInclusion(b,a))
