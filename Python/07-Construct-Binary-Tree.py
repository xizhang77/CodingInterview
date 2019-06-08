# -*- coding: utf-8 -*-

'''
// 面试题7：重建二叉树
// 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
// 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
// 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
// 图2.6所示的二叉树并输出它的头结点。
'''

'''
同 LeetCode 105
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, preorder, inorder):
        if not inorder:
            return
        val = preorder.pop( 0 )
        idx = inorder.index( val )
        root = TreeNode( val )
        root.left = self.dfs( preorder, inorder[:idx] )
        root.right = self.dfs( preorder, inorder[idx+1:] )
        
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs( preorder, inorder )