"""
Created by Kartik
"""
import random

from randomized.block import Block
from util.stack import Stack


class Sudoku:
    """
    The class that models a sudoku puzzle. Also creates a random sudoku puzzle
    """
    def __init__(self):
        self.blocks: [Block] = []
        for _ in range(9):
            self.blocks.append(Block())
        # self._blocks[0].randomize()
        # self._blocks[4].randomize()
        # self._blocks[8].randomize()

        self._space_stack = Stack[int]()
        self._retry_space_stack = Stack[int]()
        # self.create_puzzle()

    def print_puzzle(self):
        """
        Print the numbers in the puzzle to system.out
        A zero indicates an empty space
        """
        for i in [0, 3, 6]:
            print(" ")
            print(str(self.blocks[i].get_row(0)) + " " + str(self.blocks[i + 1].get_row(0)) + " " + str(
                self.blocks[i + 2].get_row(0)))
            print(str(self.blocks[i].get_row(1)) + " " + str(self.blocks[i + 1].get_row(1)) + " " + str(
                self.blocks[i + 2].get_row(1)))
            print(str(self.blocks[i].get_row(2)) + " " + str(self.blocks[i + 1].get_row(2)) + " " + str(
                self.blocks[i + 2].get_row(2)))

    def get_row(self, row_index):
        """
        Get the numbers in a specified row in the puzzle
        :param row_index: The row index for which the numbers should be returned
        :type row_index: int
        :return: The list of numbers in the specified row
        :rtype: List<int>
        """
        row = []
        for i in range(3):
            j = self.blocks[((row_index // 3) * 3) + i]
            for k in j.get_row(row_index % 3):
                row.append(k)
        return row

    def get_column(self, col_index):
        """
        Get the numbers in a specified column in the puzzle
        :param col_index: The col index for which the numbers should be returned
        :type col_index: int
        :return: The list of numbers in the specified column
        :rtype: List<int>
        """
        col = []
        for i in range(3):
            j = self.blocks[(col_index // 3) + (3 * i)]
            for k in j.get_column(col_index % 3):
                col.append(k)
        return col

    def create_puzzle_alg1(self):
        """
        Create a randomized puzzle to fill in the rest of the spots
        """

        """
        > Check if the puzzle is completed
        > If not:
            > Pick a random space and make sure it isn't already assigned a number
            > Calculate the possibilities
            > Assign a number to the space
            > If success : Add the space to the stack and break
            > If not : Do this whole process again for the last space popped from the stack
        """
        empty_spaces = self._get_empty_spaces()
        counter: int = 0
        while len(empty_spaces) is not 0:
            print(str(counter) + ". " + str(len(empty_spaces)))
            if self._retry_space_stack.is_empty():
                random_space_number = random.choice(empty_spaces)

            else:
                random_space_number = self._retry_space_stack.get_next()

            block = self.blocks[random_space_number // 10]

            possibilities = list(range(1, 10))
            for i in block.get_assigned_numbers():
                if i in possibilities:
                    possibilities.remove(i)
            for i in self.get_column(((random_space_number // 10 % 3) * 3) + (random_space_number % 10) % 3):
                if i in possibilities:
                    possibilities.remove(i)
            for i in self.get_row(((random_space_number // 10 // 3) * 3) + (random_space_number % 10) // 3):
                if i in possibilities:
                    possibilities.remove(i)
            block.set_possibilities(random_space_number % 10, possibilities)
            flag = block.assign_random_number(random_space_number % 10)

            if flag is 0:
                self._space_stack.add_item(random_space_number)

            else:
                self._retry_space_stack.add_item(random_space_number)
                reset_flag = -1
                while reset_flag is -1:
                    reset_space = self._space_stack.get_next()
                    if reset_space is not None:
                        block = self.blocks[reset_space // 10]
                        reset_flag = block.assign_random_number(reset_space % 10)
                        if reset_flag is 0:
                            self._space_stack.add_item(reset_space)
                        else:
                            self._retry_space_stack.add_item(reset_space)
                    else:
                        quit()
                    counter += 1
            empty_spaces = self._get_empty_spaces()
            counter += 1

    def create_puzzle_alg2(self):
        """
        Create a randomized puzzle to fill in the rest of the spots
        """

        """
        > Randomly assign the first square
        > Assign the first three rows --> conpletes the first row of _blocks
        > Assign the first three columns --> completes the first column of _blocks
        > Finish block 6 and block 9
        > Finish block 8
        > Finish block 5
        """
        self.blocks[0].randomize()


    def _get_empty_spaces(self):
        """
        Get a list of spaces that have not been assigned a number yet
        :return: A list that contains spaces that have not been assigned yet
        :rtype: List<int>
        """
        empty_spaces = []
        for block_number in range(9):
            for space_number in self.blocks[block_number].get_empty_spaces():
                empty_spaces.append(block_number*10 + space_number)
        return empty_spaces
