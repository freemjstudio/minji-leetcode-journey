class Solution:
    def jump(self, nums: List[int]) -> int:
        max_idx = 0 # reachable idx 
        jump_count = 0 
        end_of_jump = 0 

        for cur_idx, jump in enumerate(nums[:-1]): 
            max_idx = max(max_idx, cur_idx + jump)
            if cur_idx == end_of_jump:
                jump_count += 1
                end_of_jump = max_idx

        return jump_count  