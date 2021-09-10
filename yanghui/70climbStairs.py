class Solution:
    def climbStairs(self, n: int) -> int:
        # 我的思路是，不管前面怎么走，最后就剩1个台阶的时候，1种，2个台阶的时候2种；前面只是看得到多少条路径，分叉到最后一层，得到有多少种方法
        global comb_num
        comb_num = 0
        def count(s):
            global comb_num
            if s == 2:
                comb_num += 2
            elif s == 1:
                comb_num += 1
            else:
                steps = [1, 2]
                for step in steps:
                    count(s - step)
        count(n)
        return comb_num

    def climbStairs_Dynamic(self, n: int) -> int: # 动态规划
        import numpy as np
        steps = list(np.zeros(n + 1))
        for i, s in enumerate(steps):
            if i == 1:
                steps[i] = 1
            elif i == 2:
                steps[i] = 2
            else:
                steps[i] = steps[i - 1] + steps[i - 2]
        print(steps)
        return steps[n]

    def climbStairs_demo(self, n: int):
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        output = self.climbStairs_demo(n - 1) + self.climbStairs_demo(n - 2)
        return output


nums = 38
solution = Solution()
output = solution.climbStairs(nums)
print(output)
output = solution.climbStairs_Dynamic(nums)
print(output)

