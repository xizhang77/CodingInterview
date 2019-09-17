# -*- coding: utf-8 -*-

'''
// 面试题35：复杂链表的复制
// 题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead)，复
// 制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个
// 结点外，还有一个m_pSibling 指向链表中的任意结点或者nullptr。

同LeetCode 138: https://leetcode.com/problems/copy-list-with-random-pointer/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def dfs(self, head, hashmap):
        if not head:
            return
        if head not in hashmap:
            node = Node( head.val, None, None )
            hashmap[ head ] = node
        if head.next:
            if head.next not in hashmap:
                next_node = Node( head.next.val, None, None )
                hashmap[ head.next ] = next_node
            hashmap[ head ].next = hashmap[ head.next ]
        if head.random:
            if head.random not in hashmap:
                rand_node = Node( head.random.val, None, None )
                hashmap[ head.random ] = rand_node
            hashmap[ head ].random = hashmap[ head.random ]
            
        self.dfs( head.next, hashmap )
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return 
        
        hashmap = {}
        self.dfs( head, hashmap )
        
        return hashmap[ head ]