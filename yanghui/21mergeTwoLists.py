
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists_Iteration(self, l1: ListNode, l2: ListNode) -> ListNode:  # 迭代
        l1_key = l1
        l2_key = l2
        output = ListNode(0)
        l3 = output
        while l1_key and l2_key:
            if l1_key.val >= l2_key.val:
                l3.next = l2_key
                l2_key =l2_key.next
            else:
                l3.next = l1_key
                l1_key = l1_key.next
            l3 = l3.next
        if l1_key:
            l3.next = l1_key
        elif l2_key:
            l3.next = l2_key
        return output.next

    def mergeTwoLists_Recursion(self, l1: ListNode, l2: ListNode) -> ListNode:  # 递归
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_Recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_Recursion(l1, l2.next)
            return l2



head1 = ListNode(0)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(4)


head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)


solution = Solution()
output = solution.mergeTwoLists_Recursion(head1,head2)
print(output)