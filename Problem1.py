# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Minheap implementation
# TC: O(n log k)
# SC: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        largest = 0

        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]

# Maxheap implementation
# TC: O(n log(n-k))
# SC: O(n-k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        largest = 99999
        n = len(nums)

        for num in nums:
            heapq.heappush(maxheap, -num)
            if len(maxheap) > n-k:
                popped = heapq.heappop(maxheap)
                largest = min(largest, -popped)

        return largest

