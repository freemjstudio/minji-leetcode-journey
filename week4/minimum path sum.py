from collections import deque 

# top left : (0,0) 
# bottom right : (n-1, m-1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_path_sum = int(1e9)

        dx = [0, 1] # You can only move either down or right 
        dy = [1, 0]

        def bfs(x, y):
            nonlocal min_path_sum
            visited = [[False] * n for _ in range(m)]
            queue = deque([])
            queue.append((x, y, grid[x][y]))
          
            while queue: 
                x, y, path_sum = queue.popleft()
                visited[x][y] = True 

                if x == m-1 and y == n-1:
                    min_path_sum = min(min_path_sum, path_sum)

                for k in range(2):
                    nx, ny = x + dx[k], y + dy[k] # update the positions
                    if 0 <= nx < m and 0 <= ny < n:
                        if not visited[nx][ny]:
                            queue.append((nx, ny, path_sum + grid[nx][ny]))

        
        bfs(0, 0) 

        return min_path_sum 

