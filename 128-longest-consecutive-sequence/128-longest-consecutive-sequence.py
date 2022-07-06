class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        new = set(nums)
        for num in new:
            if num - 1  not in new:
                current = 1
                curr_num = num
                
                while curr_num + 1 in new:
                    current+=1
                    curr_num+=1
                longest = max(current, longest)
        return longest
        