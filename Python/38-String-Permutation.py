# -*- coding: utf-8 -*-

'''
// 面试题38：字符串的排列
// 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
// 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

Similar to LeetCode 47: https://leetcode.com/problems/permutations-ii/
'''

class Solution(object):
    def dfs(self, string, ans, path):
        if not string:
            ans.append( path )
            return
        i = 0
        while i < len(string):
            self.dfs( string[:i] + string[i+1:], ans, path + string[i] )
            while i + 1 < len(string) and string[i] == string[i+1]:
                i += 1
            i += 1
            
    def stringPermutations(self, string):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        string = sorted( string )
        
        ans = []
        
        self.dfs( string, ans, '' )
        
        return ans

s = Solution()
print s.stringPermutations( 'aabc' )