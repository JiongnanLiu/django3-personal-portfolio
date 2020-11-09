from copy import deepcopy
from random import sample


def get_presence(cells):
    present_in_row = [{i: False for i in range(1, 10)} for j in range(9)]
    present_in_column = [{i: False for i in range(1, 10)} for j in range(9)]
    present_in_grid = [{i: False for i in range(1, 10)} for j in range(9)]

    for row_num in range(9):
        for column_num in range(9):
            num = cells[row_num][column_num]

            if num:
                present_in_row[row_num][num] = True
                present_in_column[column_num][num] = True
                present_in_grid[row_num // 3 * 3 + column_num // 3][num] = True

    return present_in_row, present_in_column, present_in_grid


def get_possible_values(cells):
    present_in_row, present_in_column, present_in_grid = get_presence(cells)
    possible_values = {}

    for row_num in range(9):
        for column_num in range(9):
            if cells[row_num][column_num] == 0:
                possible_values[(row_num, column_num)] = [
                    num for num in range(1, 10) if
                    (not present_in_row[row_num][num]) and
                    (not present_in_column[column_num][num]) and
                    (not present_in_grid[row_num //
                                         3 * 3 + column_num // 3][num])
                ]

    return possible_values


def update(cells):
    update_again = False

    possible_values = get_possible_values(cells)
    for location in possible_values:
        if len(possible_values[location]) == 1:
            update_again = True
            cells[location[0]][location[1]] = possible_values[location][0]
            break

    if update_again:
        cells = update(cells)

    return cells


def trial_plug_in(cells, location, value):
    copied_cells = deepcopy(cells)
    copied_cells[location[0]][location[1]] = value
    copied_cells = non_class_solve(copied_cells)

    return copied_cells


def non_class_solve(cells):
    cells = update(cells)
    possible_values = get_possible_values(cells)

    if not len(possible_values):
        return cells

    min_value_num = 10
    for location in possible_values:
        value_num = len(possible_values[location])

        if not value_num:
            return False

        if value_num < min_value_num:
            min_value_num = value_num
            min_location = location

    for value in possible_values[min_location]:
        tried_cells = trial_plug_in(cells, min_location, value)
        if tried_cells:
            return tried_cells

    return False


class Puzzle:
    last_check_pos = (0, 0)

    def __init__(self, cells=None):
        if cells:
            self.cells = cells
        else:
            self.cells = [[0 for i in range(9)] for j in range(9)]

    def validate(self):
        row_count = [{num: 0 for num in range(1, 10)} for i in range(9)]
        column_count = [{num: 0 for num in range(1, 10)} for i in range(9)]
        grid_count = [{num: 0 for num in range(1, 10)} for i in range(9)]
        print(row_count)
        print(column_count)
        print(grid_count)
        for row_num in range(9):
            for column_num in range(9):
                num = self.cells[row_num][column_num]

                if num:
                    row_count[row_num][num] += 1
                    column_count[column_num][num] += 1
                    grid_count[row_num // 3 * 3 + column_num // 3][num] += 1

                    if row_count[row_num][num] > 1 or column_count[column_num][num] > 1 or grid_count[row_num // 3 * 3 + column_num // 3][num] > 1:
                        return False

        return True

    def __str__(self):
        result = ''
        for row_num in range(9):
            for column_num in range(9):
                result += str(self.cells[row_num][column_num]) + ' '

            result += '\n'

        return result

    def solve(self):

        if not self.validate():
            raise ValueError('Input invalid.')
        find = self.find_empty()
        if not find:
            return True
        '''
        result_cells = non_class_solve(self.cells)

        if not result_cells:
            raise ValueError('Input invalid.')
        else:
            self.cells = result_cells
        '''
        if not self.solver():
            raise ValueError('Input invalid.')
        return False


# ====================================================================================================

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
        #self.cells = [[0 for i in range(9)] for j in range(9)]

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
    [7, 0, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

bo = Puzzle()
# bo.print_board()
bo.puzzle_gen()
print(bo.cells)
'''
