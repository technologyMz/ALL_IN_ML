
import string

uppercase = string.ascii_uppercase  # 获取26个大写字母
lowercase = string.ascii_lowercase  # 获取26个小写字母
letters = string.ascii_letters  # 获取26个小写字母和26个大写字母

class Solution:
    def letterCasePermutation(self, s: str):
        combine_list = []
        def backtrack(remain, ununsed):
            if len(remain) == len(s):
                combine_list.append(''.join(remain))
                return
            use_list = []
            if ununsed[0] in lowercase:
                use_list = [ununsed[0], ununsed[0].upper()]
            if ununsed[0] in uppercase:
                use_list = [ununsed[0], ununsed[0].lower()]

            if not use_list:
                num = ununsed[0]
                remain.append(num)
                ununsed.pop(0)
                backtrack(remain, ununsed)
                remain.pop()
                ununsed.insert(0, num)
            else:
                left_list = ununsed[1:]
                for one_letter in use_list:
                    remain.append(one_letter)
                    backtrack(remain, left_list)
                    remain.pop()
                left_list.insert(0, ununsed[0])
        input_list = list(s)
        backtrack([], input_list)
        return combine_list

nums= "RmR"  # 注意remove的话，不能确定删除的是哪一个，可以用pop
solution = Solution()
output = solution.letterCasePermutation(nums)
print(output)
