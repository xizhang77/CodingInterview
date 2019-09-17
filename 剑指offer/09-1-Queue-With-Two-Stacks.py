# -*- coding: utf-8 -*-

'''
// 面试题9：用两个栈实现队列
// 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
// 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。


同 LeetCode 232
https://leetcode.com/problems/implement-queue-using-stacks/

队列pop：若stack2为空，将stack1中所有val全部压入stack2，然后pop stack2的栈顶元素；
		否则直接pop stack2栈顶元素
队列push：直接push [stack2 保存着queue的头部，优先pop，因此和stack1的插入操作不冲突]
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append( x )

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
        	while self.stack1:
        		self.stack2.append( self.stack1.pop(0) )

        return self.stack2.pop( 0 )