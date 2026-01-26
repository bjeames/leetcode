# rule for index flattening:
# index = row * (number_of_columns) + column

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        columns = [set() for _ in range(cols)]
        squares = [set() for _ in range(cols)]

        for i in range(rows):
            row_check = set()
            for j in range(cols):
                # check row
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_check:
                    return False
                row_check.add(board[i][j])
                
                # check column
                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                
                # check square
                box_index = (i // 3) * 3 + (j // 3)


                if board[i][j] in squares[box_index]:
                    return False
                else:
                    squares[box_index].add(board[i][j])
        return True
        