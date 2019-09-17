# -*- coding: utf-8 -*-

'''
面试题5：替换空格
题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
则输出“We%20are%20happy.”。
'''

# Solution 1
# Time: O(n)
class Solution1(object):
    def replaceSpace(self, s, a):
        """
        :type s: str
        :rtype: str
        """

        return s.replace(" ", a)

# Solution 2
# Time & Space: O(n)
class Solution2(object):
    def replaceSpace(self, s, a):
        """
        :type s: str
        :rtype: str
        """

        s = list(s)

        for i in range( len(s) ):
        	if s[i] == " ":
        		s[i] = a

       	return "".join(s)


S = Solution2()
print S.replaceSpace( "We are happy.", "%20")