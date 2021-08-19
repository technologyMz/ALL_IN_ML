"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect_DFX(self, root) :

        def add_nextpoint(point):
            if point.left != None:
                point.left.next = point.right
                point.right



# 构造二叉树t, BOTTOM-UP METHOD
#        1
#     /    \
#    2       3
#  /   \   /   \
# 4     5 6     7
right_tree = Node(3)
right_tree.left = Node(6)
right_tree.right = Node(7)


left_tree = Node(2)
left_tree.left = Node(4)
left_tree.right = Node(5)

tree1 = Node(1)
tree1.left = left_tree
tree1.right = right_tree


solution = Solution()
merged_tree = solution.connect_DFX(tree1)
print(merged_tree)


