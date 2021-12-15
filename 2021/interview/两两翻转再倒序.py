# coding: utf-8
# [1, 2, 3, 4, 5, 6, 7]
# -->
# [2, 1, 4, 3, 6, 5, 7]
# -->
# [7, 5, 6, 3, 4, 1, 2]
class Node:

    def __init__(self, val):
        self.value = val
        self.next = None


def createLinkedList(l):
    head = Node(None) # None 避免变头
    cur = head
    for i in l: # 1-7
        cur.next = Node(i)
        cur = cur.next
    return head

# def switch(head): # 保留头迭代
#     if not head or not head.next:
#         return
#     pre = head
#     cur = head.next
#     nxt = None
#     while cur and cur.next: # None->1->2->3 to None->2->1->3
#         nxt = cur.next.next # 保存3
#         cur.next.next = cur # 2->1
#         pre.next = cur.next# None->2
#         cur.next = nxt # 1->3 为什么一定需要？也可以使用 30-32 代替
#         pre = cur
#         cur = nxt
#     代替方案
#     if cur:
#         pre.next = cur
#
#         pre = None; cur = 1; nxt =3;
#         2.next = 1; None.next = 2; 1.next = 3;
#         pre = 1; cur = 3; nxt = 5;
#         4.next = 3; 1.next = 4; 3.next = 5


class Solution:
    def switch(self, head): # 无头迭代
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next

    def switch2(self, head): # 无头递归
        if not head or not head.next:
            return head
        newHead = head.next # 保存2
        head.next = self.switch2(newHead.next) # 1->上次递归的结果
        newHead.next = head # 2->1
        return newHead

    @staticmethod
    def reverse(head): # 无头迭代 1->2->3 3->2->1
        pre = None
        next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def reverse2(self, head): # 无头递归
        if not head or not head.next:
            return head
        newHead = self.reverse2(head.next)
        head.next.next = head
        head.next = None
        return newHead


def printLinkedList(head):
    cur = head
    while cur:
        print(cur.value, end=',')
        cur = cur.next


def test():
    from copy import deepcopy
    list = [1,2,3,4,5,6,7]
    print(list)
    s = Solution()
    head = createLinkedList(list)
    head = head.next
    head2 = deepcopy(head)
    head = s.switch(head)
    print('\n')
    printLinkedList(head)
    head = s.reverse(head)
    print('\n')
    printLinkedList(head)
    head2 = s.switch2(head2)
    print('\n')
    printLinkedList(head2)
    head2 = s.reverse2(head2)
    print('\n')
    printLinkedList(head2)

if __name__ == '__main__':
    test()

