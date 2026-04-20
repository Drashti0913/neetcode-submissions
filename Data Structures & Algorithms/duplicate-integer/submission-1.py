class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_number = set()

        for num in nums:
            if num in seen_number:
                return True
            seen_number.add(num)
        return False        