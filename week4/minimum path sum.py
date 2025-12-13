from collections import queue 

# top left : (0,0) 
# bottom right : (n-1, m-1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == -1:
                    new_path_sum = dfs(i, j) # check the route 
        dx = [0, 1] # You can only move either down or right 
        dy = [1, 0]
        def bfs(x, y):
            queue = queue([])
            queue.append((x, y))
            visited[x][y] = True 
            while queue: 
                x, y = queue.popleft()
                if x == n-1 and y == m-1:
                    return path_sum

                for k in range(2):
                    nx, ny = x + dx[k], y + dy[k] # update the positions
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        visited[nx][ny] += 1
                        queue.append((nx, ny))




        return answer 