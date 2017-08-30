"""
Created by Kartik
"""
import random


class Block:
    """
    The class that stores the information of one 3x3 block in a Sudoku puzzle
    The class is also responsible for creating a randomized block given the spaces of the surrounding _blocks
    """

    def __init__(self):
        self._spaces: [int][int] = []
        for _ in range(3):
            self._spaces.append([0, 0, 0])
        self._possibilities: [str] = []

    def get_row(self, row_index: int) -> [int]:
        """
        Get the contents of a given row
        :param row_index: The row index for which the contents are requested
        :type row_index: int
        :return: The contents of a requested row
        :rtype: [int]
        """
        return self._spaces[row_index]

    def get_column(self, col_index: int) -> [int]:
        """
        Get the contents of a given column
        :param col_index: The column index for which the contents are requested
        :type col_index: int
        :return: The contents of the requested column
        :rtype: [int]
        """
        return_list = []
        for space_list in self._spaces:
            return_list.append(space_list[col_index])
        return return_list

    def generate_block(self, surrounding_blocks) -> int:
        """
        Generate a puzzle based on the surrounding _blocks
        :param surrounding_blocks: An list that contains the boxes in every direction around this block
        :type surrounding_blocks: [[Block]]
        :return 0 if success, -1 if failure
        :rtype int
        """
        vertical_blocks = surrounding_blocks[0]
        horizontal_blocks = surrounding_blocks[1]

        self._possibilities = self.generate_possibility(vertical_blocks, horizontal_blocks, 0, [])
        if self._possibilities is -1:
            return -1

        return self.randomize_from_possibilities()

    def randomize_from_possibilities(self) -> int:
        """
        Create a randomized block from the list of existing possibilities
        :return: 0 if success, -1 if fail
        :rtype: int
        """
        if len(self._possibilities) is 0:
            return -1

        current_possibility = random.choice(self._possibilities)
        self._possibilities.remove(current_possibility)

        for i in self._spaces:
            for j in range(3):
                i[j] = int(current_possibility[0])
                current_possibility = current_possibility[1:]
        return 0

    def generate_possibility(self, vertical_blocks, horizontal_blocks, block_index, previous_possibilities) -> [str]:
        """
        Recursively generate the psosibilities of a certain block using the individual properties of each space in the
        block and the surrounding _blocks
        :param vertical_blocks: The _blocks above and below this certain block
        :type vertical_blocks: [Block]
        :param horizontal_blocks: The _blocks to the left and to the right of this certain block
        :type horizontal_blocks: [Block]
        :param block_index: The index of the current space in the block for which the possibility is being calculated
        :type block_index: int
        :param previous_possibilities: The list that's a combination of all the previous possibilities
        :type previous_possibilities: [str]
        :return: The list of strings that represents the possibilities in the block
        :rtype: [str]
        """

        possibilities: [int] = list(range(1, 10))
        for block in vertical_blocks:
            for space in block.get_column(block_index % 3):
                if space in possibilities:
                    possibilities.remove(space)
        for block in horizontal_blocks:
            for space in block.get_row(block_index // 3):
                if space in possibilities:
                    possibilities.remove(space)

        if len(possibilities) is 0:
            return -1

        combined_possibilities: [str] = []

        if previous_possibilities == []:
            for i in possibilities:
                combined_possibilities.append(str(i))
        else:
            for i in possibilities:
                for j in previous_possibilities:
                    if str(i) in j:
                        continue
                    else:
                        combined_possibilities.append(j + str(i))

        # Base Case
        if block_index is 8:
            return combined_possibilities

        # Recursive Case
        to_return = self.generate_possibility(vertical_blocks, horizontal_blocks, block_index + 1,
                                              combined_possibilities)
        if to_return is -1:
            return -1

        return to_return
