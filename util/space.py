"""
Created by Kartik
"""


class Space:
    """
    A class to store a single space that is referenced by each tree. Deleting a space from the list technically removes
    it from the trees
    """
    def __init__(self, number: int):
        self._number = number

    def get_space(self) -> int or None:
        """
        Get the number stored in this object
        :return: The number stored in the space
        :rtype: int
        """
        return self._number

    def remove_space(self) -> None:
        """
        Remove the number in this space and set it to None
        """
        self._number = None

    def set_space(self, number: int) -> None:
        """
        Set the number in this space to the provided number
        :param number: The number to set this space to
        :type number: int
        """
        self._number = number
