# -*- coding: utf-8 -*-

'''
// 面试题24：反转链表
// 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
// 头结点。

同LeetCode 206: https://leetcode.com/problems/reverse-linked-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iteratively
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        p, q = head, head.next
        while q:
            nq = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p, q = q, nq
        
        return p


# Recursively
class Solution2(object):
    def dfs(self, node):
        if not node or not node.next:
            return node, node
        
        head, tail = self.dfs( node.next )
        tail.next = node
        
        return head, node
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head, new_tail = self.dfs( head )
        if new_tail:
            new_tail.next = None
        
        return new_head
        