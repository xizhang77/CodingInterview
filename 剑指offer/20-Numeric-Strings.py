# -*- coding: utf-8 -*-

'''
// 面试题20：表示数值的字符串
// 题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
// 字符串“+100”、“5e2”、“-123”、“3.1416”及“-1E-16”都表示数值，但“12e”、
// “1a3.14”、“1.2.3”、“+-5”及“12e+5.4”都不是

同 LeetCode 65: https://leetcode.com/problems/valid-number/
'''

class Solution(object):
    def isFloat(self, s):
        if not s:
            return False
        
        digits = set("0123456789")
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        dec = 0
        count = 0
        for char in s:
            if char in digits:
                count += 1
            if char == '.':
                dec += 1
                continue
            if char not in digits:
                print char
                return False

        return count > 0 and dec <= 1
        
    def isInt(self, s):
        if not s:
            return False
        digits = set("0123456789")
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        count = 0
        for char in s:
            if char in digits:
                count += 1
            else:
                return False
            
        return count > 0
        
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = set(" 0123456789e-+.")
        
        for char in s:
            if char not in check:
                return False
        
        s = s.strip()
        
        if 'e' in s:
            digits = s.split("e")
            if len(digits) > 2:
                return False
            return self.isFloat( digits[0] ) and self.isInt( digits[1] )
        else:
            return self.isFloat( s )