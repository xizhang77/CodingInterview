# -*- coding: utf-8 -*-

'''
// 面试题36：二叉搜索树与双向链表
// 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
// 不能创建任何新的结点，只能调整树中结点指针的指向。

同LeetCode 426: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def preOrder(self, root):
        if not root:
            return
        
        self.preOrder( root.left )
        
        if not self.first:
            self.first = root
            
        if self.last:
            self.last.right = root
            root.left = self.last
            
        self.last = root
        
        self.preOrder( root.right )
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        
        self.first = self.last = None
        
        self.preOrder( root )
        
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first