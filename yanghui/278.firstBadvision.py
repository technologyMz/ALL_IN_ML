
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version): return True if version>=5 else False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        good_index = 0
        bad_index = n
        while (good_index <= bad_index):
            if bad_index - good_index == 1:
                return bad_index
            middle_index = good_index + int((bad_index - good_index)/2)
            if isBadVersion(middle_index):
                bad_index = middle_index
            else:
                good_index = middle_index


Solution = Solution()
print(Solution.firstBadVersion(4))