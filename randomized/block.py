"""
Created by Kartik
"""

import random
from randomized.space import Space


class Block:
    """
    One 3x3 block in a sudoku puzzle
    """

    def __init__(self):
        self._spaces = []
        for i in range(9):
            self._spaces.append(Space())

    def randomize(self):
        """
        Create a random set of numbers
        """

        a = random.randint(1, 9)
        for i in range(9):
            space = (a + i) % 9
            if space == 0:
                space = 9
            self._spaces[i] = Space(space, True)

        for _ in range(50):
            a = random.random()
            b = random.random()

            first_index = int(((a / b) * 100) % 9)

            a = random.random()
            b = random.random()

            second_index = int(((a / b) * 100) % 9)

            temp = self._spaces[first_index]
            self._spaces[first_index] = self._spaces[second_index]
            self._spaces[second_index] = temp

    def get_row(self, row_index):
        """
        Get the numbers stored in this row
        :param row_index: The row to get the numbers from this block
        :type row_index: int
        :return: The list of numbers that are in the specified row
        :rtype: List<int>
        """
        row = []
        for i in range(3):
            row.append(self._spaces[row_index * 3 + i].get_data())
        return row

    def get_column(self, col_index):
        """
        Get the numbers stored in this column
        :param col_index: The column to get the numbers from this block
        :type col_index: int
        :return: The list of numbers that are in the specified column
        :rtype: List<int>
        """
        col = []
        for i in range(3):
            col.append(self._spaces[i * 3 + col_index].get_data())
        return col

    def get_empty_spaces(self):
        """
        Get the numbers of the spaces that are empty in the block
        :return: List containing the numbers(ids) of the spaces that are empty or an empty list if the block is done
        :rtype: List<int>
        """
        empty_spaces = []
        for space_number in range(9):
            if self._spaces[space_number].get_data() == 0:
                empty_spaces.append(space_number)
        return empty_spaces

    def get_assigned_numbers(self):
        """
        Get the numbers that have been assigned already in the block
        :return: The numbers that have been used in the block
        :rtype: List<int>
        """
        assigned_numbers = []
        for space in self._spaces:
            data = space.get_data()
            if data is not 0:
                assigned_numbers.append(data)
        return assigned_numbers

    def set_possibilities(self, space_number, possibilities):
        """
        Remove the possiblities that cannot occur from the list of possibilities
        :param space_number: The number that is the id for the space which is to be randomly assigned
        :param possibilities: The numbers that can occur in this space
        """
        space = self._spaces[space_number]
        space.set_possibilities(possibilities)

    def assign_random_number(self, space_number):
        """
        Assign a random number to the space specified by the number
        :param space_number: The number that is the id for the space which is to be randomly assigned
        :type space_number: int
        :return: 0 if succes, -1 if failure
        """
        space = self._spaces[space_number]
        return space.assign_random()
