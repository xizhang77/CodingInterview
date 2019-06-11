# -*- coding: utf-8 -*-

'''
// 面试题18（一）：在O(1)时间删除链表结点
// 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。


类似于LeetCode 237 https://leetcode.com/problems/delete-node-in-a-linked-list/
只不过本题增加了对时间复杂度的要求
而且237中明确指出，node不是tail
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, head, node):
        """
        :type head: ListNode
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        if p.next:
        	p.val = p.next.val
        	p.next = p.next.next
        	return head
        else:
        	q = head
        	while q.next != p:
        		q = q.next
        	q.next = p.next
        	return head