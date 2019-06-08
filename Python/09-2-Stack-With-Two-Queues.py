# -*- coding: utf-8 -*-

'''
相关题目：用两个队列实现栈

同 LeetCode 225
https://leetcode.com/problems/implement-stack-using-queues/
'''

# Solution 1: Using two queues
'''
Stack pop: 将不为空的queue中所有元素取出并attach在另一个queue中，直到该queue只剩一个元素，pop
Stack push：将元素直接attach在不为空的queue中
'''


# Solution 2: Using one queue instead of two
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
    
    def organize(self):
        for i in range( len(self.queue) - 1 ):
            self.queue.append( self.queue.pop( 0 ) )
            
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.queue:
            self.queue.append( self.queue.pop( 0 ) )
        self.queue.append( x )
        self.organize()

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        val = self.queue.pop( 0 )  
        self.organize()
        
        return val
        
