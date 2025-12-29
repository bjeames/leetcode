from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hash_map = {}
        for row in grid:
            key = tuple(row)
            hash_map[key] = hash_map.get(key, 0) + 1

        # columns = [[] for item in grid]

        # for i in range(len(grid)):
        #     for j in range(len(grid)):
        #         columns[i].append(grid[j][i])
        # counter = 0
        # for item in columns:
        #     item = tuple(item)
        #     if item in hash_map:
        #         counter+=hash_map.get(item)
        # zip(*matrix) = transpose the matrix
        counter = 0
        for column in zip(*grid):
            if column in hash_map:
                counter+= hash_map[column]
        return counter


