class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][cols-1] >= target:
                l = 0
                r = cols - 1
                while l <= r:
                    m = (l+r)//2
                    if matrix[i][m] < target:
                        l = m + 1
                    elif matrix[i][m] > target:
                        r = m - 1
                    else:
                        return True
        return False
        