from django.shortcuts import render
from sudoku.models import Sudoku, Ranking
from .puzzle import Puzzle
# Create your views here.


def ranking(request):
    users = Ranking.objects.order_by('rank')
    '''
    rank_counter = 1
    print(users)
    
    for user in users:
        if (rank_counter <= 10):
            user.rank = rank_counter
            rank_counter += 1
        else:
            break
            '''
    return render(request, 'sudoku/sudoku.html', {'users': users})


def sudoku(request):
    users = Ranking.objects.order_by('rank')
    res = request.POST

    if res:
        cells = []

        for row_num in range(9):
            cells.append([])

            for column_num in range(9):
                current_location = 'cell-%i-%i' % (row_num + 1, column_num + 1)
                print(current_location)
                try:
                    current_num = int(res[current_location])
                except ValueError:
                    current_num = 0

                cells[row_num].append(current_num)

        my_puzzle = Puzzle(cells=cells)

        try:
            valid = my_puzzle.solve()
            if valid:
                puzzle = Puzzle()
                cells = puzzle.puzzle_gen()
                print(cells)
                return render(request, 'sudoku/sudoku.html', {'cells': cells, 'valid': True, 'users': users})
            else:
                puzzle = Puzzle()
                cells = puzzle.puzzle_gen()
                print(cells)
                return render(request, 'sudoku/sudoku.html', {'cells': my_puzzle.cells, 'new': False, 'error': False, 'users': users})

        except ValueError:
            puzzle = Puzzle()
            cells = puzzle.puzzle_gen()
            print(cells)
            return render(request, 'sudoku/sudoku.html', {'cells': cells, 'new': True, 'error': True, 'users': users})
        '''
        res = my_puzzle.solve()
        if res:
            return render(request, 'sudoku/sudoku.html', {'cells': my_puzzle.cells, 'new': False, 'error': False})
        else:
            return render(request, 'sudoku/sudoku.html', {'cells': [[0 for i in range(9)] for j in range(9)], 'new': True, 'error': True})
        '''
    else:
        puzzle = Puzzle()
        cells = puzzle.puzzle_gen()
        print(cells)
        return render(request, 'sudoku/sudoku.html', {'cells': cells, 'new': True, 'error': False, 'users': users})


""" def all_players(request):
    players = Sudoku.objects.all()
    return render(request, 'portfolio/sudoku.html', {'players': players})
 """
