class Solution:
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
