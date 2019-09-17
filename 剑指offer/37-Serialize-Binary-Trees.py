# -*- coding: utf-8 -*-

'''
// 面试题37：序列化二叉树
// 题目：请实现两个函数，分别用来序列化和反序列化二叉树。

同LeetCode 297: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inOrder(self, root, path):
        if not root:
            path.append("%")
            return
        path.append( str(root.val) )
        self.inOrder( root.left, path )
        self.inOrder( root.right, path )
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        self.inOrder( root, path )
        
        return "/".join( path )

    def dfs(self, path ):
        if not path:
            return
        val = path.pop(0)
        if val == '%':
            return None
        else:
            node = TreeNode( int( val ) )
            node.left = self.dfs( path )
            node.right = self.dfs( path )
            return node
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        path = data.split("/")
        
        return self.dfs( path )

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))