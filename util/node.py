"""
    Created by Kartik
"""
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """
    Node to store the items in the stack and the next item
    """
    def __init__(self, item: T, next_item=None) -> None:
        self._data = item
        self._next = next_item

    def get_data(self) -> T:
        """
        Get the data stored in the node
        :return: Data stored in this node
        :rtype: T
        """
        return self._data

    def get_next(self):
        """
        Get the node next to the current node in the collection
        :return: Data stored in the node
        :rtype: Node[T]
        """
        return self._next
