"""
Created by Kartik
"""
from fixed_sequence_generator.sudoku import Sudoku


class SudokuSolver:
    """
    A sudoku solver that can be used to find the difficulty of a sudoku puzzle. Solves the puzzle using the
    different legal moves that can be made, in the order of least difficult to most difficult
    """

    def single_position_on_row(self, row_index: int, sudoku: Sudoku) -> int:
        """
        Apply the single position technique on the specified row in the specified sudoku puzzle
        :param row_index: The row number for which the technique is to be applied
        :type row_index: int
        :param sudoku: The sudoku puzzle to solve
        :type sudoku: Sudoku
        """
        """
        1. Get the empty spaces in the row and the numbers in each row
        2. For each missing number check where it can be placed
        3. If there is only one spot where it can be placed: Place it there
        """
        this_row = sudoku.get_row(row_index)

        for space in this_row:
            if space is 0:

