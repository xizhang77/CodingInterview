# -*- coding: utf-8 -*-

'''
// 面试题44：数字序列中某一位的数字
// 题目：数字以0123456789101112131415…的格式序列化到一个字符序列中。在这
// 个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一
// 个函数求任意位对应的数字。

同LeetCode 400: https://leetcode.com/problems/nth-digit/
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        
        n -= 10
        numDigit = 2
        
        while n - numDigit*9*(10**(numDigit-1)) > 0:
            n -= numDigit*9*(10**(numDigit-1))
            numDigit += 1
        
        num, placer = n/numDigit, n%numDigit
        
        return int(str(10**((numDigit-1)) + num)[placer])
        


# Time and Space: O(n) 
class Solution2(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = ""
        
        i = 0
        while len(temp) <= n:
            temp += str(i)
            i += 1
        
        return int(temp[n])