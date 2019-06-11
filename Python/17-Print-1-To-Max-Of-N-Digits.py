# -*- coding: utf-8 -*-

'''
// 面试题17：打印1到最大的n位数
// 题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则
// 打印出1、2、3一直到最大的3位数即999。


这道题的考点在于大数（当n大到int型会溢出时，就要考虑用其他的数据类型来存储）
'''

# Time: O(32)
class Solution(object):
	def printDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 0:
			return
			
		digit = [''] * n
		digit[-1] = '0'
		res = 0

		while True:
			res += 1
			for i in range( n-1, -1, -1 ):
				if digit[i] == "":
					digit[i] = '0'
				temp = int(digit[i]) + res
				digit[i] = str( temp%10 )
				res = temp/10
				if not res:
					break
			print "".join(digit)
			if digit == ['9'] * n:
				break

s = Solution()
s.printDigits( 2 )