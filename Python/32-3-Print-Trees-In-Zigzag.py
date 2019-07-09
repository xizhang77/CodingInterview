# -*- coding: utf-8 -*-

'''
// 面试题32（三）：之字形打印二叉树
// 题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺
// 序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，
// 其他行以此类推。

同LeetCode 103: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        
        current = [ root ]
        flag = 1
        
        while current:
            nextLevel = []
            val = []
            for node in current:
                val.append( node.val )
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            if flag:
                ans.append( val )
            else:
                ans.append( val[::-1] )
            current = nextLevel
            flag = 1-flag
            
        return ans