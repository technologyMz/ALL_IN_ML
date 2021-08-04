def search( nums, target) -> int:
    if len(nums) == 0:
        return -1

    def compare(input_list, target, start, end):
        print(start, end)
        if start > end:   #等于的情况，可能就是middle_index值=target的情况
            return -1
        middle_index = int(start+(end-start)/2)
        if input_list[middle_index] == target:
            return middle_index
        elif input_list[middle_index] > target:
            return compare(input_list, target, start, middle_index - 1)
        else:
            return compare(input_list, target, middle_index+1, end )

    return compare(nums, target, 0, len(nums)-1)  # end的初始值需要-1


def search2(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while True:
        if left > right:   #等于的情况，可能就是middle_index值=target的情况
            return -1
        middle_index = int(left+(right-left)/2)
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            left = left
            right = middle_index - 1
        else:
            left = middle_index+1
            right = right

