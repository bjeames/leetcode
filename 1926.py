from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # make visited list of grids
        # start it with entrace inside
        # make a queue that will start with entrance

        # we want to make it to where the next row or column would be out of bounds
        # then return the number of steps it took to get there, don't add the step
         # that would take you out of bounds
        queue = deque([[entrance, 0]])
        rows_edge = len(maze) - 1
        cols_edge = len(maze[0]) - 1
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            current_lvl= len(queue)
            for _ in range(current_lvl):
                current_grid, steps = queue.popleft()
                r,c = current_grid[0], current_grid[1]
                if (
                    r == rows_edge or
                    r == 0 or
                    c == cols_edge
                    or c == 0) and [r,c] != entrance:
                    return steps
                else:
                    next_steps = [(r+1,c), (r-1,c), (r,c+1), (r, c-1)]
                    for grid in next_steps:
                        r, c = grid[0], grid[1]
                        if (
                            r <= rows_edge and  r >= 0 and
                            c <= cols_edge and c >= 0 and
                        maze[grid[0]][grid[1]] == '.' and 
                        grid not in visited):
                            queue.append([grid, steps+1])
                            visited.add((r,c))
        
        return -1





        