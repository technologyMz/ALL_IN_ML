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


    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        left = 0
        right = len(s1) - 1
        counter1 = collections.Counter(s1)
        while right < len(s2):
            counter2 = collections.Counter(s2[left:right + 1])
            if counter1 == counter2:
                return True

            if right + 1 < len(s2) and s2[right + 1] in counter1:
                right += 1
                left += 1
            else:
                left = right + 2
                right = left + len(s1) - 1
        return False


s1 ="adc"
s2 = "dcda"
solution = Solution()
print(solution.checkInclusion(s1,s2))

