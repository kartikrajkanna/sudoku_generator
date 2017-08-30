"""
Created by Kartik
"""

import random


class Space:
    """
    A single space in a sudoku puzzle
    """

    def __init__(self, number=0):
        self._space = number
        self._possibilities = []

    def set_space(self, number, fixed=False):
        """
        Set the number that this space should contain if that number is possible and return 0. If not, return -1
        :param number: The number to be assigned to the space
        :type number: int
        :param fixed: Represents whether this space's number can be changed or not
        :type fixed: bool
        :return: The status of the number set process : 0 if success, -1 if failure
        :rtype: int
        """
        if fixed:
            self._space = number
            self._possibilities = []

        if number in self._possibilities:
            self._possibilities.remove(number)
            self._space = number

    def get_data(self):
        """
        Get the data stored in this space
        :return: The number stored in the space
        :rtype: int or None
        """
        return self._space

    def set_possibilities(self, possibilities):
        """
        Remove the possiblities that cannot occur from the list of possibilities
        :param possibilities: The numbers that can occur in this space
        """
        self._possibilities = possibilities

    def assign_random(self):
        """
        Assign a random number to the space from the allowed possibilities
        :return: 0 if success, -1 if failure
        """
        self._space = 0

        if len(self._possibilities) is 0:
            return -1

        random_possibility = random.choice(self._possibilities)
        self.set_space(random_possibility)
        return 0
