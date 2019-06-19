# -*- coding: utf-8 -*-

'''
// 面试题22：链表中倒数第k个结点
// 题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
// 本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
// 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
// 值为4的结点。

同LeetCode 19
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode( None )
        temp.next = head
        
        prevq, q, p = temp, head, head
        count = 0
        
        while p:
            p = p.next
            count += 1
            if count > n:
                prevq = q
                q = q.next
        
        prevq.next = q.next
        
        return temp.next

