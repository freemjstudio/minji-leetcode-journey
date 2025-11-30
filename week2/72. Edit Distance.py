import sys 

sys.setrecursionlimit(1000000)

# Try1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        answer = int(1e9) # maximum as default

        def dfs(cur_word, count):
            nonlocal answer 
            if cur_word == word2:
                answer = min(answer, count) 
                return 
            
            if len(word1) == len(word2): # only replace ? 
                for i in range(len(word1)):
                    cur_word[i] =  word2[i]
                    dfs(cur_word, count + 1)
   
            if len(word1) > len(word2): # delete
                for i in range(len(word1)):
                    new_word = cur_word
                    new_word = new_word.replace(word1[i], "")
                    dfs(new_word, count+1)

        dfs(word1, 0)
        return answer 


# Try 2: 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else: 
                    dp[i][j] = dp[i-1][j-1]
        
        for i in dp:
            print(*i)

        return dp[n][m] 