class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return left+1, right+1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    # 二分查找
    def twoSum2(self,numbers, target):
        for left_index in range(len(numbers)):
            if numbers[left_index] > target:
                return -1, -1
            right = target - numbers[left_index]
            BS_start = left_index + 1
            BS_end = len(numbers) - 1
            while BS_start <= BS_end:
                BS_middle = BS_start + int((BS_end - BS_start) / 2)
                if numbers[BS_middle] == right:
                    right_index = BS_middle
                    return left_index + 1, right_index + 1
                elif numbers[BS_middle] < right:
                    BS_start = BS_middle + 1
                else:
                    BS_end = BS_middle - 1




input_nums =[5,25,75]
solution = Solution()
#print(solution.twoSum(input_nums, 4))
print(solution.twoSum2(input_nums, 100))
