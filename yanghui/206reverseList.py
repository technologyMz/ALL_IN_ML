# Definition for singly-linked list.
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_Iteration(self, head: ListNode) -> ListNode: # 迭代
        due = collections.deque()
        l1 = head
        while l1:
            due.append(l1)
            l1 = l1.next
        output = ListNode(-1)
        l2 = output
        while due:
            thepoint = due.pop()
            l2.next = thepoint
            l2 = l2.next
        l2.next = None
        return output.next

    # 递归
    def reverseList_Recursion(self, head: ListNode) -> ListNode: # 迭代
        due = collections.deque()
        l1 = head
        while l1:
            due.append(l1)
            l1 = l1.next
        output = ListNode(-1)
        l2 = output
        while due:
            thepoint = due.pop()
            l2.next = thepoint
            l2 = l2.next
        l2.next = None
        return output.next

head1 = ListNode(0)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

solution = Solution()
output = solution.reverseList(head1)
print(output)