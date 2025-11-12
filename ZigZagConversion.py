def convert(s: str, numRows: int) -> str:
    n = numRows
    if n == 1 or n >= len(s):
        return s

    rows = [''] * n # create a list of strings, one string per row
    going_down = False # direction indicator
    current_row = 0 # track the row we are adding to

    for character in s: # iterate over each character

        if current_row == 0 or current_row == n-1: # check if row is at top or bottom
            going_down = not going_down # switch directions if so

        rows[current_row] += character # add character to current row
        current_row += 1 if going_down else -1 # move up or down depending on direction
    
    return ''.join(rows)


if __name__ == "__main__":

    s = "PAYPALISHIRING"
    numRows = 3
    Output = "PAHNAPLSIIGYIR"

    result = convert(s, numRows)

    print(f"Expected output: {Output}")
    print(f"  Actual output: {result}")