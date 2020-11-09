from random import sample


class Sudoku:

    last_check_pos = (0, 0)

    def __init__(self, cells=None):
        '''
        bo is a 9x9 board, must be a list of lists, with length of 9 for both outer list and inner list.
        for example
        board = [
                        [7,8,0,4,0,0,1,2,0],
                        [6,0,0,0,7,5,0,0,9],
                        [0,0,0,6,0,1,0,7,8],
                        [0,0,7,0,4,0,2,6,0],
                        [0,0,1,0,5,0,9,3,0],
                        [9,0,4,0,6,0,0,0,5],
                        [0,7,0,3,0,0,0,1,2],
                        [1,2,0,0,0,7,4,0,0],
                        [0,4,9,2,0,6,0,0,7]
                        ]
        '''
        if cells:
            self.cells = cells
        else:
            self.cells = [[0 for i in range(9)] for j in range(9)]

    def solver(self):
        '''
        backtracking algorithms.
        recusive call itself to solve the next one given the current one is valid
        if all the option tried are invalid for current pos, return back to the last solve function that called this one. thus backtracking.
        '''
        find = self.find_empty()
        if not find:
            return True

        row, col = find

        for i in range(1, 10):
            # check if the number i is valid for the current position
            if self.valid(i, (row, col)):
                self.cells[row][col] = i  # if valid, makes it equal to i

                if self.solver():  # recursively call itself to solve the next box assuming the current pos is i
                    return True

            # if i is invalid for pos, set it back to 0 and try another i.
            self.cells[row][col] = 0
        # in a recusive call of solve function, if all the number i (from 1 to 9) is checked for the current position and invalid.
        return False
        # then return false anad return back to the last solve function that called this one, and try another i for the last position.

    def valid(self, num, pos):

        # Check row
        for i in range(len(self.cells[0])):
            if self.cells[pos[0]][i] == num and pos[1] != i:
                return False
        # Check column
        for j in range(len(self.cells)):
            if self.cells[j][pos[1]] == num and pos[0] != j:
                return False

        # Check small box
        box_x = pos[1] // 3  # column
        box_y = pos[0] // 3  # row

        for i in range(box_y*3, box_y*3 + 3):  # loop each row
            for j in range(box_x*3, box_x*3 + 3):  # loop each column
                if self.cells[i][j] == num and (i, j) != pos:
                    return False

        return True

    def print_board(self):
        for i in range(len(self.cells)):
            if i % 3 == 0 and i != 0:
                print('------------------------')
            for j in range(len(self.cells[0])):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(str(self.cells[i][j]))
                else:
                    print(str(self.cells[i][j]) + ' ', end='')

    def find_empty(self):
        if self.last_check_pos == (0, 0):
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    if self.cells[i][j] == 0:
                        self.last_check_pos = (i, j)
                        return (i, j)
        else:
            # start from the row that last checked
            for i in range(self.last_check_pos[0], len(self.cells)):
                for j in range(len(self.cells[i])):
                    if self.cells[i][j] == 0:
                        return (i, j)
        return None

    def puzzle_gen(self):
        base = 3
        side = base*base
        # pattern for a baseline valid solution
        def pattern(r, c): return (base*(r % base)+r//base+c) % side
        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s): return sample(s, len(s))
        rBase = range(base)
        rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base*base+1))
        # produce board using randomized baseline pattern
        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares), empties):
            board[p // side][p % side] = 0
        self.cells = board
        return board


'''
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

bo = Sudoku(board)
bo.print_board()
bo.solver()
print('========================')
bo.print_board()
'''
bo = Sudoku()
bo.puzzle_gen()
bo.print_board()
