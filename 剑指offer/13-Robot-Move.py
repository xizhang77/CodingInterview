# -*- coding: utf-8 -*-

'''
// 面试题13：机器人的运动范围
// 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
// 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
// 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
// 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
'''


class Solution(object):
	def check(self, limit, i, j):
		count = 0
		while i:
			count += i%10
			i = i/10
		while j:
			count += j%10
			j = j/10
		if count <= limit:
			return True
		else:
			return False

	def backtracking(self, m, n, limit, i, j, path):
		if not self.check( limit, i, j ):
			return
		self.count += 1
		direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
		for d in direct:
			ii, jj = i + d[0], j + d[1]
			if 0 <= ii < m and 0 <= jj < n and (ii,jj) not in path:
				path += [(ii,jj)]
				self.backtracking( m, n, limit, ii, jj, path )

	def robotMove(self, m, n, limit):
		"""
		:type m: int
		:type n: int
		:type limit: int
		:rtype: int
		"""
		self.count = 0
		self.backtracking( m, n, limit, 0, 0, [(0,0)] )

		return self.count


s = Solution()
print s.robotMove(10,10,5) # 21
print s.robotMove(20,20,15) #359 
print s.robotMove(10,10,-5)