# -*- coding: utf-8 -*-

'''
// 面试题45：把数组排成最小的数
// 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
// 接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数
// 字能排成的最小数字321323。

同 LeetCode 179: https://leetcode.com/problems/largest-number/
'''

class Solution(object):
    def compare(self, num1, num2):
        num1, num2 = str(num1), str(num2)
        if int( num1 + num2 ) > int( num2 + num1 ):
            return True
        else:
            return False
        
    def solver(self, nums):
        if not nums:
            return [ ]
        target = nums[0]
        first = []
        last = []
        same = 1
        for num in nums[1:]:
            if target == num:
                same += 1
                continue
            if self.compare( target, num ):
                first.append( num )
            else:
                last.append( num )
        return self.solver( first ) + [ str(target) ]*same + self.solver( last )
            
        
    def smallestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        if len( set(nums) ) == 1 and nums[0] == 0:
            return "0"
                
        sortNum = self.solver( nums )
        
        return "".join( sortNum )