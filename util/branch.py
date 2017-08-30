"""
Created by Kartik
"""
from util.space import Space


class Branch:
    """
    A branch in the Tree structure. Is a leaf if there are no children in this branch in the tree
    """
    def __init__(self, space: Space):
        self._space: Space = space
        self._children: [Branch] = []

    def add_children(self, children) -> None:
        """
        Add a list of children to this branch
        :param children: List of children to add to this Branch
        :type children: [Branch]
        """
        for child in children:
            self._children.append(child)
