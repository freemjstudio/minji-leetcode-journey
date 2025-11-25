# https://leetcode.com/problems/longest-increasing-subsequence/description/
from types import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i-1]: 
                dp[i] = max(dp[i-1] + 1, dp[i]) 
            else: 
                dp[i] = dp[i-1]
        return max(dp) 

# edge case : 
# [4,10,4,3,8,9]

# O(N²)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i): # count if the number is smaller than current number (nums[i])
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                
        return max(dp) 

# it has binary search solution ! 