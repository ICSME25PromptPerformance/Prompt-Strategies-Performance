class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2, 4)
        6
        """
        BitStatusUtil.check([states, stat])
        # Use bitwise OR to add the status
        return states | stat

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6, 2)
        True
        """
        BitStatusUtil.check([states, stat])
        # Use bitwise AND to check if status is present
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The status after removing the specified status, int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6, 2)
        4
        """
        BitStatusUtil.check([states, stat])
        # Use bitwise AND with NOT to remove the status
        return states & ~stat

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even, if not, raise ValueError.
        :param args: Parameters to be checked, list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2, 3, 4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} is less than 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")