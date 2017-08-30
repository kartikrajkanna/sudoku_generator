"""
Created by Kartik
"""
from fixed_sequence_generator.block import Block
from util.stack import Stack


class Sudoku:
    """
    The class that models a sudoku puzzle. Also creates a random sudoku puzzle
    """
    def __init__(self):
        self._blocks: [Block] = []
        for _ in range(9):
            self._blocks.append(Block())

    def print_puzzle(self) -> None:
        """
        Print the numbers in the puzzle to system.out
        A zero indicates an empty space
        """
        for i in [0, 3, 6]:
            print(" ")
            print(str(self._blocks[i].get_row(0)) + " " + str(self._blocks[i + 1].get_row(0)) + " " + str(
                self._blocks[i + 2].get_row(0)))
            print(str(self._blocks[i].get_row(1)) + " " + str(self._blocks[i + 1].get_row(1)) + " " + str(
                self._blocks[i + 2].get_row(1)))
            print(str(self._blocks[i].get_row(2)) + " " + str(self._blocks[i + 1].get_row(2)) + " " + str(
                self._blocks[i + 2].get_row(2)))

    def get_row(self, row_index: int) -> [int]:
        """
        Get the numbers in a specified row in the puzzle
        :param row_index: The row index for which the numbers should be returned
        :type row_index: int
        :return: The list of numbers in the specified row
        :rtype: List<int>
        """
        row = []
        for i in range(3):
            j = self._blocks[((row_index // 3) * 3) + i]
            for k in j.get_row(row_index % 3):
                row.append(k)
        return row

    def get_column(self, col_index: int) -> [int]:
        """
        Get the numbers in a specified column in the puzzle
        :param col_index: The col index for which the numbers should be returned
        :type col_index: int
        :return: The list of numbers in the specified column
        :rtype: List<int>
        """
        col = []
        for i in range(3):
            j = self._blocks[(col_index // 3) + (3 * i)]
            for k in j.get_column(col_index % 3):
                col.append(k)
        return col

    def create_puzzle(self):
        """
        Create the puzzle by creating one block at a time
        """
        for i in range(9):
            self.create_block(i)

    def create_block(self, block_index: int) -> int:
        """
        Try to randomly create a block. If this does not work, recursively fix it by going to previous blocks
        :param block_index: The index of the current block being created
        :type block_index: int
        :return:
        :rtype:
        """
        block = self._blocks[block_index]

        # Calculate surrounding indices
        top_block_index = (block_index + 3) % 9
        bottom_block_index = (block_index - 3) % 9
        left_block_index = (block_index // 3 * 3) + ((block_index % 3) + 1) % 3
        right_block_index = (block_index // 3 * 3) + ((block_index % 3) - 1) % 3

        # Get the blocks from the indices
        top_block = self._blocks[top_block_index]
        bottom_block = self._blocks[bottom_block_index]
        left_block = self._blocks[left_block_index]
        right_block = self._blocks[right_block_index]

        flag = block.generate_block([[top_block, bottom_block], [left_block, right_block]])

        while flag is -1:
            # print("Cannot Generate Block", block_index)
            self.recreate_block(block_index-1)
            flag = block.generate_block([[top_block, bottom_block], [left_block, right_block]])

        # print("Generated Block", block_index)
        # self.print_puzzle()

        return flag

    def recreate_block(self, block_index: int) -> None:
        """
        Try to randomly create a block. If this does not work, recursively fix it by going to previous blocks
        :param block_index: The index of the current block being created
        :type block_index: int
        """
        flag = self._blocks[block_index].randomize_from_possibilities()
        if flag is -1:
            if block_index is 0:
                print("Error")
            # print(block_index)
            self.recreate_block(block_index-1)
            self.create_block(block_index)
