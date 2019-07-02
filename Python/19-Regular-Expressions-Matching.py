# -*- coding: utf-8 -*-

'''
// 面试题19：正则表达式匹配
// 题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'
// 表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题
// 中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
// 和"ab*ac*a"匹配，但与"aa.a"及"ab*a"均不匹配。

同 LeetCode 10 [Hard]: https://leetcode.com/problems/regular-expression-matching/
'''

class Solution(object):
    def isEqual(self, char1, char2):
        return char1 == char2 or char2 == '.'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        
        m, n = len(s), len(p)
        
        dp = [ [False]*(n+1) for _ in range(m+1) ]
        dp[0][0] = True
        
        for i in range( m + 1 ):
            for j in range( 1, n + 1 ):
                if i >= 1 and p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and self.isEqual( s[i-1], p[j-1] )
                elif p[j-1] == '*':
                    dp[i][j] = (j >= 2 and dp[i][j-2]) or ( i >= 1 and dp[i-1][j] and self.isEqual( s[i-1], p[j-2] ) )
        
        return dp[-1][-1]