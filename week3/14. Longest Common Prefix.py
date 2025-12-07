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
        if len(strs) == 1:
            return strs[0]

        answer = ""
        is_prefix = True
        min_length = 200
        for i in range(len(strs)):
            min_length = min(min_length, len(strs[i]))

        for i in range(min_length):
            for j in range(len(strs) -1):
                if strs[j][i] != strs[j+1][i]:
                    is_prefix = False
                    break 
                else: 
                    char = strs[j][i] 
            if is_prefix:
                answer += char
            else:
                break 
        return answer 
    


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # ["flower","flow","flight"]
        answer = ""
        strs = sorted(strs)
        print(strs) # ['flight', 'flow', 'flower'] sorted in lexicographical order
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return answer
            answer += first[i]
        return answer 