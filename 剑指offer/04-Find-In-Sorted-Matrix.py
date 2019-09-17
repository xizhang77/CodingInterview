# -*- coding: utf-8 -*-

'''
面试题4：二维数组中的查找

题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。
'''

# Solutuion 1 [one can start from either (0, n-1) or (m-1,0) ]
# Time: O(n)
class Solution1(object):
    def findInMatrix(self, matrix, target):
        """
        :type nums: List[List[int]]
        :rtype: bool
        """

        if not matrix or not matrix[0]:
        	return False

        m, n = len(matrix), len(matrix[0])

        i, j = m-1, 0

        while i >= 0 and j < n:
        	if matrix[i][j] > target:
        		i -= 1
        	elif matrix[i][i] < target:
        		j += 1
        	else:
        		return True

        return False