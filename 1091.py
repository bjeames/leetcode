from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        if n_rows == 1 and n_cols == 1:
            if grid[0][0] == 0:
                return 1
        target = (n_rows-1, n_cols -1)
        vertex_and_path = [((0,0), 1)]
        bfs_queue = deque(vertex_and_path)
        visited = set()

        while bfs_queue:
            current_vertex, current_path = bfs_queue.popleft()
            r, c = current_vertex
            if grid[r][c] == 1:
                continue
            choices = [
                (r+1, c), (r-1, c),
                (r,c+1), (r, c-1), 
                (r+1, c+1), (r+1, c-1),
                (r-1, c+1), (r-1, c-1)]
            for neighbor in choices:
                if(
                    neighbor not in visited and
                    neighbor[0] < n_rows and neighbor[0]>=0 and
                    neighbor[1] < n_cols and neighbor[1]>=0
                ):
                    if neighbor == target and grid[neighbor[0]][neighbor[1]] == 0:
                        return current_path + 1

                    else:
                        visited.add(neighbor)
                        bfs_queue.append([neighbor, current_path + 1])
        return -1