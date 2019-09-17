# -*- coding: utf-8 -*-

'''
// 面试题18（二）：删除链表中重复的结点
// 题目：在一个排序的链表中，如何删除重复的结点？例如，在图3.4（a）中重复
// 结点被删除之后，链表如图3.4（b）所示。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1: Set / Hash Table
class Solution1(object):
    def deleteNode(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        check = set()

        prev = ListNode( None )
        prev.next = head
        p = head
        while p:
        	if p.val not in check:
        		check.add( p.val )
        		prev = p
        	else:
        		prev.next = p.next

        	p = prev.next

        return head


# Solution 2
class Solution2(object):
    def deleteNode(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = head

        while p:
        	if p.next and p.next.val == p.val:
        		p.next = p.next.next
        	else:
        		p = p.next