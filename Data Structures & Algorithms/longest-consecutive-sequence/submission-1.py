class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        num_set = set(nums)
        long_sub = 1
        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                curr_sub = 1
            
                while curr_num +1 in num_set:
                    curr_num += 1
                    curr_sub += 1
                long_sub = max(long_sub, curr_sub)
        return long_sub
        