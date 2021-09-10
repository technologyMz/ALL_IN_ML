# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

class Solution:
    def minimumTotal(self, triangle) -> int:
        mum = triangle[::-1]
        for layer_index, one_layer in enumerate(mum):
            if layer_index == 0:
                continue
            print(layer_index)
            print(one_layer)
            for element_index, one_element in enumerate(one_layer):
                print(one_element)
                print(mum[layer_index - 1])
                print(mum[layer_index - 1][element_index], mum[layer_index - 1][element_index + 1])
                print(min(mum[layer_index - 1][element_index], mum[layer_index - 1][element_index + 1]))
                mum[layer_index ][element_index] = one_element + min(mum[layer_index - 1][element_index], mum[layer_index - 1][element_index + 1])
        return mum[-1][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
solution = Solution()
output = solution.minimumTotal(triangle)
print(output)
