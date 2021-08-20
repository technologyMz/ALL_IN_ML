# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 
        dummy = ListNode(0, head) #给最前面增加了一个节点 相当于left在-1的位置
        left = dummy
        right = head
        for i in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

    def removeNthFromEnd_demo(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)

n = 2

solution = Solution()
output = solution.removeNthFromEnd(head, n)
print(output)