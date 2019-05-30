#在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
#示例 1:
#输入: 4->2->1->3
#输出: 1->2->3->4
#示例 2:
#输入: -1->5->3->4->0
#输出: -1->0->3->4->5


# 没看懂O(nlogn)的算法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 将所有的ListNode的值取下来
        if head is None:
            return None
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        val_list.sort()
        # 逆序取出，建立链表
        ptr = ListNode(val_list.pop())
        while len(val_list)!=0:
            x = val_list.pop()
            new_node = ListNode(x)
            new_node.next = ptr
            ptr = new_node
        return ptr
        
