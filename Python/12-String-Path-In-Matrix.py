# -*- coding: utf-8 -*-

'''
// 面试题12：矩阵中的路径
// 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
// 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
// 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
// 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
// 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
// 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
// A B T G
// C F C S
// J D E H


同LeetCode 79: https://leetcode.com/problems/word-search/

'''



from collections import Counter
class Solution(object):
    def preCheck(self, board, word, m, n):
        wordCount = Counter(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in wordCount:
                    wordCount[ board[i][j] ] -= 1
        
        for key in wordCount:
            if wordCount[ key ] > 0:
                return False
        
        return True
        
    def backtracking(self, board, word, i, j, m, n, path):
        if self.ans:
            return
        if not word:
            self.ans = True
            return
        direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
        for d in direct:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n and (ii,jj) not in path and board[ii][jj] == word[0]:
                self.backtracking( board, word[1:], ii, jj, m, n, path + [(ii,jj)])
                
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return word == ''
        
        m, n = len(board), len(board[0])
        self.ans = False
        
        if not self.preCheck( board, word, m, n ):
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.backtracking( board, word[1:], i, j, m, n, [(i,j)])
        
        return self.ans