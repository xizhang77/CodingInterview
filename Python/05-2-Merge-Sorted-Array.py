# -*- coding: utf-8 -*-

'''
这道题也出现在《剑指Offer》 2.3.2字符串章节的“相关题目”中，故复制过来一起分析。
'''
'''
LeetCode 88 
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

# Solution 1: Insert from end to start [书中做法]
# Time: O(m+n); Space: O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        p = m + n - 1
        
        while i != p:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1


# Solution 2: Insert from start to end
# Time: O(m+n); Space: O(m)
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        
        i = j = 0
        for k in range( m + n ):
            if j == n or ( i < m and j < n and temp[i] < nums2[j] ):
                nums1[k] = temp[i]
                i += 1
            elif i == m or ( i < m and j < n and temp[i] >= nums2[j] ):
                nums1[k] = nums2[j]
                j += 1
        
        