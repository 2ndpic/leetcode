# 给你链表的头节点 head 和一个整数 k 。 
# 
#  交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
# 输出：[7,9,6,6,8,7,3,0,9,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1], k = 1
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：head = [1,2], k = 1
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：head = [1,2,3], k = 2
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目是 n 
#  1 <= k <= n <= 105 
#  0 <= Node.val <= 100 
#  
#  Related Topics 链表 
#  👍 7 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for i in range(k - 1):
            p1 = p1.next
        cur = p1.next
        while cur:
            cur = cur.next
            p2 = p2.next
        p1.val, p2.val = p2.val, p1.val
        return head

# leetcode submit region end(Prohibit modification and deletion)
