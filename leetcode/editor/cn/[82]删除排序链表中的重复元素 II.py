# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
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
#  👍 521 👎 0
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, None)
        visited = [0] * 209
        cur = head
        while cur:
            visited[cur.val + 100] += 1
            cur = cur.next
        cur = head
        new_cur = dummy
        while cur:
            if visited[cur.val + 100] > 1:
                cur = cur.next
            else:
                new_cur.next = cur
                new_cur = cur
                cur = cur.next
                new_cur.next = None

        return dummy.next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-200, head)
        p = dummy # 记录当前新链的末节点
        while p and p.next:
            q = p.next
            while q and p.next.val == q.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
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
        牢记变量代表的循环不变量
        head作为原输入的指针进行链表扫描，【确保进入最外层循环时的head不会与上一节点值相同】
        tail用来表示当前重建的有效链表的结尾
        head的插入时机：
            head作为最后一个节点
            head还有后面的节点，但是head值不与其相同
        """
        dummy = ListNode(-200)
        tail = dummy
        while head:
            if head.next is None or head.val != head.next.val:
                tail.next = head
                tail = tail.next
            while head.next and head.val == head.next.val:
                head = head.next
            head = head.next
        tail.next = None
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)