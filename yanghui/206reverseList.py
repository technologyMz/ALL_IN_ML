# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:



head1 = ListNode(0)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(4)

solution = Solution()
output = solution.reverseList(head1)
print(output)