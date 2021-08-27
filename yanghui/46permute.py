import copy
class Solution:
    def permute(self, nums):
        combine_list = []

        def backtrack(remain_list, unused_list, first):
            if first == nums[-1]:
                combine_list.append(remain_list)
                return

            while unused_list:
                i = unused_list[0]
                first = i
                remain_list.append(i)
                unused_list.remove(i)
                backtrack(remain_list, unused_list, first)
                remain_list.remove(i)
                unused_list.append(i)

        first = nums[0]
        nums.remove(first)
        backtrack([first], nums, first)


nums= [1,2,3,4]
solution = Solution()
output = solution.permute(nums)
print(output)
