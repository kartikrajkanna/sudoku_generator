"""
Created by Kartik
"""
from util.space import Space
from util.branch import Branch


class Tree:
    """
    A tree structure to store the different routes that can be taken to create a valid block
    """
    def __init__(self):
        self._prototype: [[Space]] = []
        for i in range(9):
            self._prototype.append([])
            for j in range(1, 10):
                self._prototype[i].append(Space(j))
        self._nodes: [Branch] or None = None

    def make_tree(self, previous_branches: [int], tree_level: int=0) -> [Branch]:
        """
        Create a tree using the prototype
        :rtype: [Branch]
        """
        valid_branches: [Branch] = []
        for space in self._prototype[tree_level]:
            if space.get_space() not in previous_branches:
                branch = Branch(space)
                if tree_level is 8:
                    valid_branches.append(branch)
                else:
                    new_previous_branches = previous_branches.copy()
                    new_previous_branches.append(space.get_space())
                    returned_children = self.make_tree(new_previous_branches, tree_level+1)
                    if returned_children is None:
                        return None
                    branch.add_children(returned_children)
                    valid_branches.append(branch)

        if len(valid_branches) is 0:
            return None
        else:
            return valid_branches
