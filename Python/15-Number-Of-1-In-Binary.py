# -*- coding: utf-8 -*-


'''
// 面试题15：二进制中1的个数
// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。


同LeetCode 191: https://leetcode.com/problems/number-of-1-bits/
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        flag = 1
        
        for i in range(32):
            if n & flag:
                count += 1
            flag <<= 1
        
        return count