"""
    Created by Kartik
"""

from typing import TypeVar, Generic

from util.node import Node

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Stack to store history of which sudoku spaces were assigned
    """

    def __init__(self):
        self._head = None

    def add_item(self, item: T) -> None:
        """
        Add a new item to the stack
        :param item: Data pertaining to the next item to add to the stack
        :type item: T
        :return: Nothing
        :rtype: None
        """
        self._head = Node(item, self._head)

    def get_next(self) -> T or None:
        """
        Return the data contained by the next Node on the stack
        :return: The data in the next node on the stack
        :rtype: T or None
        """
        if self._head is not None:
            to_return = self._head.get_data()
            self._head = self._head.get_next()
            return to_return
        else:
            return None

    def is_empty(self) -> bool:
        """
        Check if the current stack is empty
        :return: true if the stack is empty and false if not
        :rtype: bool
        """
        if self._head is not None:
            return False
        return True
