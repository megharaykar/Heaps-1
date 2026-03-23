# https://leetcode.com/problems/merge-k-sorted-lists/

# Minheap solution
# TC: O(N log k)
# SC: O(k)

import heapq

class Solution:
    def mergeKLists(self, lists):
        minheap = []
        
        # push initial nodes
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minheap, (l.val, i, l))  # add index as tie-breaker
        
        dummy = ListNode(-1)
        curr = dummy
        
        while minheap:
            val, i, node = heapq.heappop(minheap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))
        
        return dummy.next