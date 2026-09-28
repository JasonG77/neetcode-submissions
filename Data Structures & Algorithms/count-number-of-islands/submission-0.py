from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Start with the base case:
        if not grid:
            return 0
        #define variables
        rows, cols = len(grid), len(grid[0])
        islands = 0 
        visited = set()
        #do BFS to mark the rest of the island as visited
        def bfs(r, c):
            #Think your base cases for this search and how BFS algo works
            q = deque([(r, c)]) #tuples as are immutable
            visited.add((r, c)) # for sets use .add() operation
            #process the nodes by the order of the queue
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                #now search thru every direction
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and 
                        grid[nr][nc] == '1' and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        #loop through the grid:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands




                


             
        