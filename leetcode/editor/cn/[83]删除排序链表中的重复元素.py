# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,1,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序排列 
#  
#  Related Topics 链表 
#  👍 511 👎 0
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        维护循环不变量
        保证head在最外层是属于前面没有值相同节点的状态
        tail作为重建链表的尾节点
        """
        dummy = ListNode()
        tail = dummy
        while head:
            tail.next = head
            while head.next and head.next.val == head.val:
                head = head.next
            head = head.next
            tail = tail.next
            tail.next = None
        return dummy.next

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        递归
        """
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
