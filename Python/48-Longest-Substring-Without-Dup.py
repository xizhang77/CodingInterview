# -*- coding: utf-8 -*-

'''
// 面试题48：最长不含重复字符的子字符串
// 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
// 字符串的长度。假设字符串中只包含从'a'到'z'的字符。

同LeetCode 3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

# Time and Space: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        ans = 0
        
        temp = []
        
        for char in s:                
            if char in temp:
                while temp and temp[0] != char:
                    temp.pop(0)
                if temp:
                    temp.pop(0)
            
            temp.append( char )
            ans = max( ans, len(temp) )
        
        return ans