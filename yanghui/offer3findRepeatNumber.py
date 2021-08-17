class Solution:
    def findRepeatNumber(self, nums):
        # for i in range(len(nums)):  #这样问题太多了。。。。
        i = 0
        while i < len(nums):
            if nums[i] == i:  # 改成换了之后先不自增i，在同一个位置上一直换
                i += 1
                continue
            if i != nums[i]:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                exchange_id =nums[i]
                temp = nums[exchange_id]
                nums[exchange_id] = nums[i]
                nums[i] = temp
                print(nums)
                # if nums[i] == nums[nums[i]]:  # 换过去之后需要再加一次判断，很奇怪别人都没这么写，但是不这样[3, 4, 2, 0, 0, 1]这个就错了
                if nums[i] == nums[nums[i]] and i != nums[i]: # 需要增加一层判断，否则对于[0,2,3,1,1]的情况就会报错
                    return nums[i]
        return None
    def findRepeatNumber2(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

nums = [3, 4, 2, 0, 0, 1]
nums = [0,2,3,1,1]
nums = [x-1 for x in  [8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18]]
print(nums)
solution = Solution()
print(solution.findRepeatNumber(nums))