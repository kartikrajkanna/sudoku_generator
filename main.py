from fixed_sequence_generator.sudoku import Sudoku
import timeit


def creating_sudoku():
    """
    Function to create a sudoku puzzle
    :return:
    :rtype:
    """
    sudoku = Sudoku()
    sudoku.create_puzzle()

print(timeit.timeit(creating_sudoku, number=1) * 1000)
