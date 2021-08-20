"""
# Definition for a Node.
"""
import collections

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect_DFX(self, root) :
        if not root:
            return root
        doing_due = collections.deque([root])
        todo_due = collections.deque([root])

        while todo_due:
            todo_due = collections.deque()
            while doing_due:
                the_point = doing_due.popleft()
                if doing_due:
                    the_point.next = doing_due[0]
                else:
                    the_point.next = None
                if the_point.left or the_point.right:
                    todo_due.append(the_point.left)
                    todo_due.append(the_point.right)
            doing_due = todo_due


        # # 用了递归，和list，但是不知道怎么改变root本身的值
        # cur_list = [root]
        # def make_next(cl):
        #     nl = []
        #     for index, one_point in enumerate(cl):
        #         if index == len(cl) -1 :
        #             one_point.next = None
        #         else:
        #             one_point.next = cl[index + 1]
        #
        #         if one_point.left or one_point.right:
        #             nl.append(one_point.left)
        #             nl.append(one_point.right)
        #     return nl
        #
        # while cur_list:
        #     cur_list = make_next(cur_list)
        #
        # return root



        #
        # doing_due = collections.deque()
        # todo_due = collections.deque([root])
        #
        # while todo_due:
        #     last_point = todo_due.pop()
        #     last_point.next = None
        #     while the_due:
        #         right_point = the_due.pop()
        #         right_point.next = last_point
        #         last_point = right_point


        # while open_due:
        #     thepoint = open_due.popleft()
        #     due.append(thepoint)
        #     if thepoint.left or thepoint.right:
        #         open_due.append(thepoint.left)
        #         open_due.append(thepoint.right)
        #
        # while due:
        #     thepoint = due.popleft()

        print(due)


# 构造二叉树t, BOTTOM-UP METHOD
#                1
#         /            \
#        2              3
#     /    \        /      \
#    4      5      6        7
#  /  \   /  \    /  \    /   \
# 8    9 10   11 12   13 14   15


right_tree3 = Node(7)
right_tree3.left = Node(14)
right_tree3.right = Node(15)

right_tree2 = Node(6)
right_tree2.left = Node(12)
right_tree2.right = Node(13)


right_tree1 = Node(3)
right_tree1.left = right_tree2
right_tree1.right = right_tree3


left_tree3 = Node(5)
left_tree3.left = Node(10)
left_tree3.right = Node(11)

left_tree2 = Node(4)
left_tree2.left = Node(8)
left_tree2.right = Node(9)

left_tree1 = Node(2)
left_tree1.left = left_tree2
left_tree1.right = left_tree3

tree1 = Node(1)
tree1.left = left_tree1
tree1.right = right_tree1


solution = Solution()
merged_tree = solution.connect_DFX(tree1)
print(merged_tree)


