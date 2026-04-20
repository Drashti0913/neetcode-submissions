class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        # Use nlargest function for cleaner code
        return heapq.nlargest(k, count.keys(), key=count.get)
        