class Solution:
    def findRepeatNumber(self, nums):
        i = 0
        while i < len(nums) + 1:
            if nums[i] == i+1:  # 改成换了之后先不自增i，在同一个位置上一直换
                i += 1
                continue
            else:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                exchange_id =nums[i] - 1
                temp = nums[exchange_id]
                nums[exchange_id] = nums[i]
                nums[i] = temp
                print(nums)
                if nums[i] == nums[nums[i] - 1] and nums[i] - 1 != i:  # 换过去之后需要再加一次判断，很奇怪别人都没这么写，但是不这样[3, 4, 2, 0, 0, 1]这个就错了
                    return nums[i]
        return None

nums = [1,3,4,2,2]
nums = [8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18]
solution = Solution()
print(solution.findRepeatNumber(nums))