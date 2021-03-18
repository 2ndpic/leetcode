# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 734 👎 0
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        stack = []
        cur = head
        while right:
            right -= 1
            left -= 1
            if left <= 0:
                stack.append(cur)
            cur = cur.next

        for i in range((right - left + 1)//2):
            stack[i].val, stack[-1-i].val = stack[-1-i].val, stack[i].val
        return head

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        在left之前的节点作为头节点，后面的节点采用头插法
        """
        dummy = ListNode(next=head)
        left_head = dummy
        for _ in range(left - 1):
            left_head = left_head.next
        cur = left_head.next
        for _ in range(right - left):
            p = cur.next
            cur.next = p.next
            p.next = left_head.next
            left_head.next = p
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
