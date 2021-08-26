
import copy

class Solution:
    def combine(self, n: int, k: int):
        input_list = list(range(1, n+1))
        combine_list = []
        if k > n :
            return -1

        def backtrack(remain_list, unused_list, k):
            if len(unused_list) < k:
                return
            if k == 0:
                combine_list.append(remain_list[:])
                return

            while unused_list:
                i = unused_list[0]
                left_list = copy.deepcopy(unused_list)
                if k > 0:
                    remain_list.append(i)
                    left_list.remove(i)
                    backtrack(remain_list, left_list, k-1)
                    remain_list.remove(i)
                    left_list.append(i)
                    unused_list.remove(i)
                else:
                    break

        remain_list = []
        backtrack(remain_list, input_list, k)
        return combine_list




n = 4
k = 2
solution = Solution()
output = solution.combine(n,k)
print(output)
