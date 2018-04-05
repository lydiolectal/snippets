# sudoku solver that uses recursive depth-first search.
# by Lydia Ding, 03/12/18

import copy

def solve(puzzle):
    # find 0-valued spaces.
    spaces = [(r, c) for r in range(9) for c in range(9) if puzzle[r][c] == 0]
    return solve_helper(puzzle, spaces)

def solve_helper(puzzle, spaces):
    # if we've solved it -- i.e., all spaces filled -- return puzzle.
    if len(spaces) == 0: return puzzle
    # coordinates of the current blank we're trying to fill.
    curRow, curCol = spaces[0][0], spaces[0][1]
    # values that already exist in the row, col -- nums we cannot use.
    # values already in the 3x3 square that can't be used.
    used = set(puzzle[curRow] + [puzzle[row][curCol] for row in range(9)] +
        [puzzle[row][col] for row in range(curRow//3 * 3, curRow//3 * 3+ 3)
            for col in range(curCol//3 * 3, curCol//3 * 3 + 3)])
    possibleNums = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(used)
    # won't loop if there are no possibleNums
    for num in possibleNums:
        newPuzzle = copy.deepcopy(puzzle)
        newPuzzle[curRow][curCol] = num
        answer = solve_helper(newPuzzle, spaces[1:])
        if answer: return answer
    return False

if __name__ == "__main__":
    puzzle = [
    [0, 0, 0, 4, 0, 8, 0, 1, 0],
    [0, 0, 7, 0, 0, 1, 0, 0, 9],
    [0, 1, 3, 9, 2, 6, 0, 0, 0],
    [3, 0, 0, 5, 0, 0, 2, 6, 7],
    [9, 0, 0, 0, 0, 0, 0, 0, 8],
    [2, 8, 6, 0, 0, 7, 0, 0, 4],
    [0, 0, 0, 7, 9, 2, 6, 4, 0],
    [6, 0, 0, 8, 0, 0, 9, 0, 0],
    [0, 2, 0, 6, 0, 3, 0, 0, 0]
    ]

    ''' solution:
    puzzle = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 3, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 7, 2],
    ]'''

    # puzzle = [
    # [2, 0, 0, 7, 4, 3, 8, 6, 1],
    # [4, 3, 1, 8, 6, 5, 9, 2, 7],
    # [8, 7, 6, 1, 9, 2, 5, 4, 3],
    # [3, 8, 7, 4, 5, 9, 2, 1, 6],
    # [6, 1, 2, 3, 8, 7, 4, 9, 0],
    # [5, 4, 9, 2, 1, 6, 7, 3, 8],
    # [7, 6, 3, 5, 3, 4, 1, 8, 9],
    # [9, 2, 8, 6, 7, 1, 3, 0, 0],
    # [1, 0, 0, 9, 3, 8, 6, 7, 2],
    # ]

    # puzzle = [
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    print(solve(puzzle))
