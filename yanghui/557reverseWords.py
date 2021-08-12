class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        output_list = []
        for one_str in str_list:
            one_str_list = list(one_str)
            left_index = 0
            right_index = len(one_str) - 1
            while left_index <= right_index:
                temp = one_str_list[left_index]
                one_str_list[left_index] = one_str_list[right_index]
                one_str_list[right_index] = temp
                left_index +=1
                right_index -=1
            output_list.append(''.join(one_str_list))
        s = ' '.join(output_list)
        print(s)



s ="Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))
