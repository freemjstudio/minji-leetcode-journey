"""
1. [:white_check_mark: Easy] Valid Parentheses
 • https://leetcode.com/problems/valid-parentheses/
2. [:white_check_mark: Easy] Longest Common Prefix
 • https://leetcode.com/problems/longest-common-prefix/
3. [:warning: Medium] Jump Game II
 • https://leetcode.com/problems/jump-game-ii/
4. [:warning: Medium] Add Two Numbers
 • https://leetcode.com/problems/add-two-numbers/
5. [:fire: Hard] Minimum Window Substring
 • https://leetcode.com/problems/minimum-window-substring/ (편집됨) 

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        is_prefix = True
        min_length = 200
        for i in range(len(strs)):
            min_length = min(min_length, len(strs[i]))

        for i in range(min_length):
            char = strs[i][i]
            for j in range(len(strs) -1):
                if strs[j][i] != strs[j+1][i]:
                    is_prefix = False
                    break 
            if is_prefix:
                answer += char
            else:
                break 
        return answer 