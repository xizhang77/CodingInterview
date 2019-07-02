# -*- coding: utf-8 -*-

'''
// 面试题23：链表中环的入口结点
// 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，
// 环的入口结点是结点3。

同LeetCode 142: https://leetcode.com/problems/linked-list-cycle-ii/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
# O(n) memory
# Using an array to store all the visited node
# return node if it's already existed in the array

# Solution 2
# O(1) memory
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check if there exists a cycle; Count the length
        slow = fast = head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                count += 1
                slow = slow.next
                while fast != slow:
                    count += 1
                    slow = slow.next
                break
        if count == 0:
            return None

        p = q = head
        step = 0
        while step < count:
            p = p.next
            step += 1
        
        while p != q:
            p = p.next
            q = q.next
        
        return q