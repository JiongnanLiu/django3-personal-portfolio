from django.shortcuts import render
from .models import Sudoku
from .puzzle import Puzzle
# Create your views here.


def sudoku(request):
    res = request.POST

    if res:
        cells = []

        for row_num in range(9):
            cells.append([])

            for column_num in range(9):
                current_location = 'cell-%i-%i' % (row_num + 1, column_num + 1)

                try:
                    current_num = int(res[current_location])
                except ValueError:
                    current_num = 0

                cells[row_num].append(current_num)

        my_puzzle = Puzzle(cells=cells)

        try:
            valid = my_puzzle.solve()
            if valid:
                return render(request, 'sudoku/sudoku.html', {'cells': [[0 for i in range(9)] for j in range(9)], 'valid': True})
            else:
                return render(request, 'sudoku/sudoku.html', {'cells': my_puzzle.cells, 'new': False, 'error': False})

        except ValueError:
            return render(request, 'sudoku/sudoku.html', {'cells': [[0 for i in range(9)] for j in range(9)], 'new': True, 'error': True})
        '''
        res = my_puzzle.solve()
        if res:
            return render(request, 'sudoku/sudoku.html', {'cells': my_puzzle.cells, 'new': False, 'error': False})
        else:
            return render(request, 'sudoku/sudoku.html', {'cells': [[0 for i in range(9)] for j in range(9)], 'new': True, 'error': True})
        '''
    else:
        return render(request, 'sudoku/sudoku.html', {'cells': [[0 for i in range(9)] for j in range(9)], 'new': True, 'error': False})


""" def all_players(request):
    players = Sudoku.objects.all()
    return render(request, 'portfolio/sudoku.html', {'players': players}) """
