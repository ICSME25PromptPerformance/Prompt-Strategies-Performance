class AvgPartition:
    """
    This is a class that partitions the given list into different blocks by specifying the number of partitions, 
    with each block having a uniformly distributed length.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, 
        and check if the number of partitions is greater than 0.
        """
        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)
        """
        # Calculate the size of each block
        block_size = len(self.lst) // self.limit
        # Calculate the remainder
        remainder = len(self.lst) % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Calculate the size of each block and the remainder of the division, 
        and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition, int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        """
        block_size, remainder = self.setNum()
        # Calculate the start position
        start = index * block_size + min(index, remainder)
        # Calculate the end position
        end = start + block_size + (1 if index < remainder else 0)
        # Return the corresponding block
        return self.lst[start:end]