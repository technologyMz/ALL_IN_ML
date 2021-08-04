class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            middle_index = left + int((right-left)/2)
            if nums[middle_index] > target:
                right = middle_index - 1
            elif nums[middle_index] == target:
                return middle_index
            else:
                left = middle_index + 1

        # 注意left==right的时候，需要再判断target和nums[left]的关系
        if target > nums[left]:
            return left + 1
        else:
            return left


Solution = Solution()
# print(Solution.searchInsert([1,3,5,6], 0))
# print(Solution.searchInsert([1,3,5,6], 1))
# print(Solution.searchInsert([1,3,5,6], 2))
print(Solution.searchInsert([1,3,5,6], 7))
