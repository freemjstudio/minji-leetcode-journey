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
