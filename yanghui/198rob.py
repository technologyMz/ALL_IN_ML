class Solution:
    def rob(self, nums) -> int:
        max_nums = nums[:]
        for index, _ in enumerate(nums):
            if index == 0:
                max_nums[index] = nums[index]
            elif index == 1:
                max_nums[index] = max(nums[index], nums[index - 1])
            else:
                max_nums[index] = max(nums[index]+ max_nums[index -2], max_nums[index - 1])
        return max_nums[-1]

nums = [1,4,4,3,2]
solution = Solution()
output = solution.rob(nums)
print(output)
