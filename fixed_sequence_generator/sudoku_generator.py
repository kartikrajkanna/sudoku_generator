"""
Created by Kartik
"""
from fixed_sequence_generator.sudoku import Sudoku


class SudokuGenerator:
    """
    A class to generate a sudoku puzzle with spaces in it from an already generated sudoku puzzle
    """
    def __init__(self, sudoku: Sudoku):
        self._sudoku = sudoku

    def generate(self):
        """
        Generate the spaces in the sudoku puzzle based on the different difficulty rules
        :return:
        :rtype:
        """
        raise NotImplementedError


class RandomSudokuGenerator(SudokuGenerator):
    """
    A class to generate a sudoku puzzle with spaces in it from an already generated sudoku puzzle.
    Generates an easy puzzle
    """

    def __init__(self, sudoku: Sudoku):
        self.__sudoku = sudoku

    def generate(self):
        """
        Generate the puzzle using an algorithm to make an easy puzzle
        The algorithm is:


        :return:
        :rtype:
        """


class EasySudokuGenerator(SudokuGenerator):
    """
    A class to generate a sudoku puzzle with spaces in it from an already generated sudoku puzzle.
    Generates an easy puzzle
    """
    def __init__(self, sudoku: Sudoku):
        self.__sudoku = sudoku

    def generate(self):
        """
        Generate the puzzle using an algorithm to make an easy puzzle
        The algorithm is:


        :return:
        :rtype:
        """
