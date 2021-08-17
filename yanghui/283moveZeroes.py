class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

    def moveZeroes1(self, nums):
        zero_index = 0
        nozero_index = 1
        while zero_index < nozero_index and nozero_index < len(nums):
            if nums[zero_index] != 0:
                zero_index += 1
                nozero_index += 1
            elif nums[nozero_index] == 0:
                nozero_index += 1
            else:
                temp = nums[zero_index]
                nums[zero_index] = nums[nozero_index]
                nums[nozero_index] = temp
                zero_index += 1
                nozero_index += 1
        return nums

    # 这个是从逻辑上保证了，right和left都！=的时候，一定是right==left
    # 牛的
    def moveZeroes2(self, nums):
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums

input_nums =[0,1,0,3,12]
solution = Solution()
# print(solution.moveZeroes(input_nums))
# print(solution.moveZeroes1(input_nums))
print(solution.moveZeroes2(input_nums))
