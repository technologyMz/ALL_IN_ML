import copy
class Solution:
    def permute(self, nums):
        combine_list = []

        def backtrack(remain_list, unused_list):
            if len(remain_list) == len(nums):
                combine_list.append(remain_list[:])
                return

            print('unused_list', unused_list)
            for i in unused_list:
                print(i,unused_list)
                left_list = unused_list[:]
                remain_list.append(i)
                left_list.remove(i)
                print(remain_list, left_list)
                backtrack(remain_list, left_list)
                remain_list.remove(i)
                left_list.append(i)
            print('backtrack', unused_list)


        backtrack([], nums)
        return combine_list

    def permute2(self, nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                print(i, nums[i], tmp)
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

    def permute3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


nums= [1,2,3,4]
solution = Solution()
output = solution.permute(nums)
print(output)
