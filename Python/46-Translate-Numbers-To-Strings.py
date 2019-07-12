# -*- coding: utf-8 -*-

'''
// 面试题46：把数字翻译成字符串
// 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻
// 译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例
// 如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和
// "mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

同LeetCode 91: https://leetcode.com/problems/decode-ways/
'''

# Time and Space: O(n)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [0] * ( len(s) + 2 )
        dp[0] = dp[1] = 1
        
        for i in range( len(s) ):
            if s[i] == '0':
                if i > 0 and (s[i-1] == '1' or s[i-1] == '2'):
                    dp[i+2] += dp[i]
            else:
                if i == 0:
                    dp[i+2] = 1
                else:
                    dp[i+2] += dp[i+1]
                    if 10 < int(s[i-1:i+1]) <= 26:
                        dp[i+2] += dp[i]
        return dp[-1]