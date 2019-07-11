# -*- coding: utf-8 -*-

'''
// 面试题41：数据流中的中位数
// 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
// 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
// 那么中位数就是所有数值排序之后中间两个数的平均值。

同 LeetCode 295 [Hard]: https://leetcode.com/problems/find-median-from-data-stream/
'''

# Time: O(logn); Space: O(n)
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.len_min = self.len_max = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.len_max == 0:
            heapq.heappush( self.maxheap, num )
            self.len_max += 1
            return
        
        if self.len_max == self.len_min:
            if num >= self.maxheap[0]:
                heapq.heappush( self.maxheap, num )
            else:
                heapq.heappush( self.minheap, - num )
                heapq.heappush( self.maxheap, - heapq.heappop( self.minheap ) )
            self.len_max += 1        
        else:
            if num >= self.maxheap[0]:
                heapq.heappush( self.maxheap, num )
                heapq.heappush( self.minheap, - heapq.heappop( self.maxheap ) )
            else:
                heapq.heappush( self.minheap, - num )
            self.len_min += 1
        
            
    def findMedian(self):
        """
        :rtype: float
        """
        if self.len_max > self.len_min:
            return self.maxheap[0]*1.0
        else:
            return (self.maxheap[0] - self.minheap[0])*1.0/2
