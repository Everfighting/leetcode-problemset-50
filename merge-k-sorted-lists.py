#合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
#示例:
#
#输入:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#输出: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        cur = head
        
        nodes = []
        for listnode in lists:
            while listnode:
                nodes.append(listnode.val)
                listnode = listnode.next
        
        nodes = sorted(nodes)
        
        for val in nodes:
            cur.next = ListNode(val)
            cur = cur.next
        
        return head.next
