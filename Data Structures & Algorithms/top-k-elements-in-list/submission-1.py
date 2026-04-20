import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # If k equals array length, return all elements
        if k == len(nums):
            return nums
        
        # Count frequency of each number
        count = Counter(nums)
        
        # Use min-heap to keep track of top k elements
        # Heap elements are tuples: (frequency, number)
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            # If heap size exceeds k, remove the least frequent element
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the numbers from the heap
        ans = [0] * k
        for i in range(k - 1, -1, -1):
            ans[i] = heapq.heappop(heap)[1]
        
        return ans