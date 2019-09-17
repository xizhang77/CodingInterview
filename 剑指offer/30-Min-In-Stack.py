# -*- coding: utf-8 -*-

'''
// 面试题30：包含min函数的栈
// 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
// 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。

同LeetCode 155: https://leetcode.com/problems/min-stack/
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.minimum = x
        else:
            self.minimum = min( self.minimum, x )
            
        self.stack.append( [x, self.minimum] )

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimum = self.getMin()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]


           