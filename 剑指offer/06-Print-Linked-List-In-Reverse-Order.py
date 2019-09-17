# -*- coding: utf-8 -*-

'''
面试题6：从尾到头打印链表
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。

需要注意：是否可以修改链表结构（既翻转链表再print）
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def printReverseList(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ans = []

        while head:
        	ans.append( head.val )
        	head = head.next

        return ans[::-1]