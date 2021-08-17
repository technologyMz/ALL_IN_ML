class Solution:
    def sortedSquares(self, nums):
        square_list = [x*x for x in nums]
        square_list.sort()
        return square_list
    def sortedSquares1(self, nums):
        pos_list = []
        neg_list = []
        for x in nums:
            if x < 0:
                neg_list.insert(0, x * x)
            else:
                pos_list.append(x * x)
        output_list = []
        i,j =0,0
        while i < len(pos_list) and j < len(neg_list):
            print(i,j,pos_list[i], neg_list[j])
            if pos_list[i] < neg_list[j]:
                output_list.append(pos_list[i])
                i = i + 1
            else:
                output_list.append(neg_list[j])
                j = j + 1

        # 增加如果其中一个指针到头了，把剩下的直接拿进来
        if i < len(pos_list):
            output_list.extend(pos_list[i:])
        if j < len(neg_list):
            output_list.extend(neg_list[j:])
        return output_list

    def sortedSquares2(self,nums):
        left = 0
        right = len(nums) - 1
        output_list = []
        while left <= right:
            if nums[left]* nums[left] < nums[right] * nums[right]:
                output_list.insert(0, nums[right]*nums[right])
                right = right - 1
            else:
                output_list.insert(0, nums[left]*nums[left])
                left = left + 1
        return output_list


solution = Solution()
print(solution.sortedSquares2([-4,-1,0,3,10]))