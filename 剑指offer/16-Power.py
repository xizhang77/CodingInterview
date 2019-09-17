# -*- coding: utf-8 -*-

'''
// 面试题16：数值的整数次方
// 题目：实现函数double Power(double base, int exponent)，求base的exponent
// 次方。不得使用库函数，同时不需要考虑大数问题。

同LeetCode 50: https://leetcode.com/problems/powx-n/
'''
# Time: O(32)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = - n
        
        if n%2 == 0:
            return self.myPow( x*x, n/2)
        else:
            return x * self.myPow( x*x, n/2)