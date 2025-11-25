from types import List 

# https://leetcode.com/problems/jump-game/

# First Trial : O(2^n)
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        answer = False 

        def dfs(cur_index):
            nonlocal answer
            if cur_index >= len(nums)-1:
                answer = True 
                return 
            num = nums[cur_index]
            for jump in range(1, num+1):
                next_index = cur_index + jump
                dfs(next_index)
        dfs(0)

        return answer
 
 # Second Trial : O(N)
class Solution2:
    def canJump(self, nums: List[int]) -> bool: 
        max_index = 0
        
        for i, jump in enumerate(nums): 
            if i > max_index: # this is unreachable  
                return False 
            max_index = max(max_index, i + jump)

        if max_index >= len(nums)-1:
            return True 
        return False
        