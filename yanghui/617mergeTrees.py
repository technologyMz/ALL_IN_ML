# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees_BFS(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 如果 t1和t2中，只要有一个是null，函数就直接返回
        if not (t1 and t2):
            return t2 if not t1 else t1
        merged = TreeNode(t1.val + t2.val)
        due = collections.deque([merged])
        due1 = collections.deque([t1])
        due2 = collections.deque([t2])

        while due1 or due2:
            node_merged = due.popleft()
            node1 = due1.popleft()
            node2 = due2.popleft()

            if node1.left and node2.left:
                node_merged.left = TreeNode(node1.left.val + node2.left.val)
                due.append(node_merged.left)
                due1.append(node1.left)
                due2.append(node2.left)
            elif node1.left:
                node_merged.left = node1.left
            elif node2.left:
                node_merged.left = node2.left


            if node1.right and node2.right:
                node_merged.right = TreeNode(node1.right.val + node2.right.val)
                due.append(node_merged.right)
                due1.append(node1.right)
                due2.append(node2.right)
            elif node1.right:
                node_merged.right = node1.right
            elif node2.right:
                node_merged.right = node2.right
        return merged

    def mergeTrees_demo(self, t1, t2):

        # 如果 t1和t2中，只要有一个是null，函数就直接返回
        if not (t1 and t2):
            return t2 if not t1 else t1
        queue = [(t1, t2)]
        while queue:
            r1, r2 = queue.pop(0)
            r1.val += r2.val
            # 如果r1和r2的左子树都不为空，就放到队列中
            # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left:
                r1.left = r2.left
            # 对于右子树也是一样的
            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right:
                r1.right = r2.right
        return t1


#t1 = [1,3,2,5]
# 构造二叉树t1, BOTTOM-UP METHOD
right_tree = TreeNode(2)

left_tree = TreeNode(3)
left_tree.left = TreeNode(5)
left_tree.right = None

tree1 = TreeNode(1)
tree1.left = left_tree
tree1.right = right_tree


#t2 = [2,1,3,None,4,None,7]
# 构造二叉树t2, BOTTOM-UP METHOD
right_tree = TreeNode(3)
right_tree.left = None
right_tree.right = TreeNode(7)

left_tree = TreeNode(1)
left_tree.left = None
left_tree.right = TreeNode(4)

tree2 = TreeNode(2)
tree2.left = left_tree
tree2.right = right_tree

print(tree1)
print(tree2)


solution = Solution()
merged_tree = solution.mergeTrees(tree1, tree2)
print(merged_tree)